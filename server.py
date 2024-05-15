import socket
import os

socket.setdefaulttimeout(1) 

CHUNKSIZE = 1_000_000

sock = socket.socket()
sock.bind(("", 33333))
sock.listen(1)

print("Waiting for connection ...")

while True:
    try:
        client, addr = sock.accept()
        print("connected with {}".format(addr))

    except socket.timeout:
        print("Waiting for connection ...")