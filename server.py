import socket
import os

socket.setdefaulttimeout(10) 

#CHUNKSIZE = 1_000_000

#socket object initiated
sock = socket.socket()
#socket bind on localhost:33333
sock.bind(("", 33333))
#socket listens and one connection is allowed
sock.listen(1)

print("Waiting for connection ...")

while True:
    try:
        #client = socket information & addr is only the ip address
        client, addr = sock.accept()
        print("connected with {}".format(addr))
        filepath = client.recv(1600).decode()
        
        filename = str(filepath).split("/")
        
        
        
        f = open(filename[-1], "w")
        
        data = client.recv(1024).decode()
        while data:
            
            f.writelines(str(data))
            data = client.recv(1024).decode()
            
        f.close()    
        print("Fertig gelesen")

    except socket.timeout:
        print("Waiting for connection ...")