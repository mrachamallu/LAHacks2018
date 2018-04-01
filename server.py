
import socket
import time


TCP_IP = '127.0.0.1'
TCP_PORT = 5005 #any port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
var=0
while 1:
  conn.send(str(var).encode())  # echo
  print(str(var))
  if var==100:
    var=0
  else:
   var +=1
   time.sleep(0.05)

conn.close()