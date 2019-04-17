import struct
import socket

def wrap_around(number):
    return number & 0xffffffff

HOST = '172.16.75.128'
PORT = 2997

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(4)
data += s.recv(4)
data += s.recv(4)
data += s.recv(4)

numbers = struct.unpack("IIII", data) #convert to big endian numbers
result = sum(numbers)
result = wrap_around(result)
payload = struct.pack("I", result) #convert to little endian

print payload
s.send(payload) 
print s.recv(1024)
s.close()


