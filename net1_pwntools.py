from pwn import *
import struct

sh = remote('172.16.75.128', 2998)

input = sh.recv()
print input #input is the hex_string in LITTLE-ENDIAN from server
print repr(input)
print input.encode('hex')

converted = struct.unpack('i', input)[0]
print converted #converted is the number BIG-ENDIAN

#sh.interactive()
sh.sendline(str(converted))
print sh.recv()


sh.close()
