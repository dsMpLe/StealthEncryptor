import socket
import os

socket.setdefaulttimeout(10)

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
        
        print("Recieved: {}".format(filepath))

        relfile = os.path.relpath(filepath)

        dir_path = os.path.dirname(relfile)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        with open(relfile, "wb") as wfile:
            while True:
                data = client.recv(1024)
                if not data:
                    break
                wfile.write(data)


    except socket.timeout:
        print("[i] Waiting for connection ...")