import socket
import os
import python_encryptor
from time import sleep
CHUNKSIZE = 1_000_000

while True:
    sock = socket.socket()
    sock.connect(('localhost', 33333))

    filepath = input("Please type in the full path to your file you want to send\nSyntax: C:/folder/.../file\n")

    if filepath == None:
        print("Something went wrong. Please check your syntax!")
        print("Program stopped!")
        exit(1)

    sock.sendall(filepath.encode())
    sleep(3)
    file = open(filepath, "r")
    data = file.read(1024)
    while data:
        sock.send(data.encode())
        data = file.read(1024)
        
    print("{} ist leer".format(filepath))
    sleep(3)
    sock.close()