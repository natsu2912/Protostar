import struct
import socket

HOST = '172.16.75.128'
PORT = 2998
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(4)
#! These lines are used for debug purpose !#
#print data 
#print repr(data)
#print data.encode('hex')
number = struct.unpack("I", data)[0] #convert hex_string (string of an integer, in LITTLE-ENDIAN) received from server (or another client) to an integer 
s.send(str(number))
print s.recv(1024)
s.close()
