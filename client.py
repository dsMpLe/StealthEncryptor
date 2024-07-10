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
    
    key = python_encryptor.key_generate()
    
    for file in txt_files:
        sock = socket.socket()
        sock.connect(('localhost', 33333))
        file_path = path + "/" + file
        sock.sendall(file.encode())
        sleep(3)
        file = open(file_path, "r")
        data = file.read(1024)
        while data:
            sock.send(data.encode())
            data = file.read(1024)
            
        print("{} ist leer".format(file))
        sleep(3)
        sock.close()


        
        print("{} will be opened now!".format(file_path))
        file_data = open(file_path, "r")
        print("{} got opened now!".format(file_path))
        data = file_data.read()
        print("{} got read in!".format(file_path))
        file_data.close()
        print("{} got encrypted!".format(file_path))
        python_encryptor.encrypt(data, file_path, key)
