from liblo import *

import sys 
import time

import re

matrix = open("data_train1.txt", "w+")



class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self):
        ServerThread.__init__(self, 5000)
        self.GL=[]

    #receive accelrometer data
    @make_method('/muse/acc', 'fff')
    def acc_callback(self, path, args):
        acc_x, acc_y, acc_z = args
        # print ("%s %f %f %f" % (path, acc_x, acc_y, acc_z))

    #receive EEG data
    @make_method('/muse/eeg', 'ffff')
    def eeg_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        # print ("%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear))

    #handle unexpected messages
    @make_method(None, None)
    def fallback(self, path, args, types, src):
        """ print("Unknown message \
        \n\t Source: '%s' \
        \n\t Address: '%s' \
        \n\t Types: '%s ' \
        \n\t Payload: '%s'" \
        % (src.url, path, types, args))"""
        word1 = "relative"
        word2 = "absolute"
        word3 = "score"
        if re.search(word1, path) or re.search(word2, path) or re.search(word3, path):
            # print(args)
            self.GL = self.GL + args
            if re.search("theta_session_score", path):
                matrix.write(str(self.GL))
                matrix.write("\n")

                self.GL = []

try:
    server = MuseServer()
except ServerError:
    # print("err")
    sys.exit()


server.start()

if __name__ == "__main__":
    for i in range(100):
        time.sleep(1)

matrix.close()
