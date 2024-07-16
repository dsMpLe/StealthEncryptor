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

print("[i] Waiting for connection ...")

while True:
    try:
        #client = socket information & addr is only the ip address
        client, addr = sock.accept()
        print("[+] connected with {}".format(addr))
        filepath = client.recv(1600).decode()
        
        print(filepath)
        
        filename = str(filepath).split("/")
        print("[i] Recieved filename is {}".format(filename[-1]))
        f = open(filename[-1], "wb")
        while True:
            data = client.recv(1024)
            if not data:
                break
            f.write(data)
                
        f.close()    
        print("[i] Fertig gelesen")

    except socket.timeout:
        print("[i] Waiting for connection ...")