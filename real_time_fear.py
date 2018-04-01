from liblo import *

import sys 
import time
import final_train
import re
import socket
import time








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
        #  print("Unknown message \
        # \n\t Source: '%s' \
        # \n\t Address: '%s' \
        # \n\t Types: '%s ' \
        # \n\t Payload: '%s'" \
        # % (src.url, path, types, args))
        word1 = "relative"
        word2 = "absolute"
        word3 = "score"
        if re.search(word1, path) or re.search(word2, path) or re.search(word3, path):
            # print(args)
            self.GL = self.GL + args
            if re.search("theta_session_score", path):
                prediction=final_train.fear_factor(self.GL)
                print("prediction={}".format(prediction))
                prediction=int(prediction*100)
                ###can do some processing before sending###
                conn.send((str(prediction).zfill(3)).encode())#just write the prediction to the port 
                self.GL = []


#####################server code#######################
TCP_IP = '127.0.0.1'
TCP_PORT = 5005 #any port number

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((TCP_IP, TCP_PORT))
my_socket.listen(1)

conn, addr = my_socket.accept()
print ('Connection address:', addr)
#####################server code#######################


try:
    server = MuseServer()
except ServerError:
    # print("err")
    sys.exit()


server.start()

if __name__ == "__main__":
    for i in range(1000):
        time.sleep(1)

matrix.close()
