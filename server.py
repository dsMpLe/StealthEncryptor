import socket
import pathlib

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

        # Convert Windows-style path to Linux-style path
        filepath = pathlib.PureWindowsPath(filepath).as_posix()

        # Create relative path
        relfile = pathlib.Path(".").joinpath(filepath)

        relfile.mkdir(parents=True, exist_ok=True)

        """with open(relfile, "wb") as wfile:
            while True:
                data = client.recv(1024)
                if not data:
                    break
                wfile.write(data)"""


    except socket.timeout:
        print("[i] Waiting for connection ...")