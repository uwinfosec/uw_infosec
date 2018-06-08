#!/usr/bin/python

import socket

# target host
host='localhost'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# address of the target - ip/hostname , port number
addr=(host, 10000)
sock.connect(addr)

try:
    msg=b"waddup\n"
    sock.sendall(msg)
except socket.errno as e:
    print("Socket error ", e)
finally:
    sock.close()

