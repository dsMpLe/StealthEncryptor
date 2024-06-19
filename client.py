import socket
import os
import python_encryptor
from time import sleep
CHUNKSIZE = 1_000_000

while True:
    
    
    path = input("Please type in the full path to your folder you want to send\nSyntax: C:/folder/.../file\n")
    
    
    
    if path == None:
        print("Something went wrong. Please check your syntax!")
        print("Program stopped!")
        exit(1)

    files = os.listdir(path)
    txt_files = [file for file in files if file.endswith(".txt")]
    
    
    
    for file in txt_files:
        sock = socket.socket()
        sock.connect(('localhost', 33333))
        file = path + "/" + file
        sock.sendall(file.encode())
        sleep(3)
        file = open(file, "r")
        data = file.read(1024)
        while data:
            sock.send(data.encode())
            data = file.read(1024)
            
        print("{} ist leer".format(file))
        sleep(3)
        sock.close()