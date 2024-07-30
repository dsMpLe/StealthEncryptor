#!/bin/python3
#python encryptor which takes an input and encrypts it

#2024-05-10 - Dennis Ortlieb

import sys
from cryptography.fernet import Fernet



#banner
print("-" * 50)
print("Author: dsMpLe")
print("Project: Python Encryptor for files")
print("Read Me: This program is used for encrypting files, \
deleting them and creating new files with the encrypted \
input")
print("Creation Date: 2024-05-10")
print("-" * 50)



#generates 256-bit key
def key_generate():

    
    key = Fernet.generate_key()

    output_file = open("key.txt", "wb")
    output_file.write(key)
    output_file.close()

    return key


#encryption of data in file
def encrypt(data, file, key):
    #initialize key
    f = Fernet(key)

    #encrypt data
    token = f.encrypt(data)

    #open/create the file
    f_file = open(file, "wb")

    #write the file
    f_file.write(token)
    f_file.close


#decryption
def decrypt(encrypted_token, file, key):
    f = Fernet(key)

    data = f.decrypt(encrypted_token)
    
    print("*" * 50)
    print("Your file contains following content:")
    print("*" * 50)
    print(str(data))

    write_to_file = input("[+] Do you want to write the data back in the file again? [yes/no]\n")

    if write_to_file == "yes":
        
        f_file = open(file, "wb")

        #write the file
        f_file.write(data)
        f_file.close



#checks if required input is given
if len(sys.argv) >= 2:
   
    #write the filename in 'file'
    input_file = sys.argv[1]

    #open file
    file_data = open(input_file, "rb")

    #write context of the file in 'data'
    data = file_data.read()
    file_data.close()

    key_file = input("Please provide the path to your key file!\n")

    if key_file == "":
        key = key_generate()
    
    else:
        key_file = open(key_file, "rb")

        key = key_file.read()
        key_file.close()

    #user can decide weather he wants to encrypt or decrypt
    action = input("E: encrypt\nD: decrypt\n")
    
    if action.lower() == "e":

        output_file = input("Please type in the path to your output file!\
If the file does not exist, it is going to be\
created!\n")
        
        print("{} is going to be encrypted!".format(input_file))
        encrypt(data, output_file, key)
        print("{} has been encrypted! Your key is in a seperate file!\n".format(input_file))
        
    elif action.lower() == "d":

        decrypt(data, input_file, key)
