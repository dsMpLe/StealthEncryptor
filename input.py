def params():

    host_ip = str(input("[+] Please type in the ip-address of the server, you want to send the data: "))
    
    path = input("[+] Please type in the full path to your folder you want to send\nSyntax: C:/folder/.../file\n")
    
    if path == None:
        print("[!] Something went wrong. Please check your syntax!")
        print("[!] Program stopped!")
        exit(1)

    return host_ip, path