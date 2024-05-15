import socket
import os

CHUNKSIZE = 1_000_000

sock = socket.socket()
sock.connect(('localhost', 33333))