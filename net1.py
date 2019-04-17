import struct
import socket

HOST = '172.16.75.128'
PORT = 2998
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(4)
print data
print repr(data)
print data.encode('hex')
number = struct.unpack("I", data)[0]
s.send(str(number), 4)
print s.recv(1024)
s.close()
