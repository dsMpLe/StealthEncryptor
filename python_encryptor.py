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








#methods
#encryption
def encrypt(data, file):
    #generates encryption/decryption key
    key = Fernet.generate_key()
    f = Fernet(key)

    key = str(key)
    key_array = key.split("'")
    key = key_array[1]
    
    output_file = open("key.txt", "w")
    output_file.write(key)

    token = f.encrypt(str.encode(data))

    #open/create the file
    f_file = open(file, "w")

    token = str(token)
    token_array = token.split("'")
    token = token_array[1]

    #write the file
    f_file.write(token)
    f_file.close


#decryption
def decrypt(encrypted_token, key):
    f = Fernet(key)
    data = f.decrypt(encrypted_token)

    data = str(data)
    data_array = data.split("'")
    data = data_array[1]
    
    print("*" * 50)
    print("Your file contains following content:")
    print("*" * 50)
    print(data)



#checks if required input is given
if len(sys.argv) == 2:
   
    #write the filename in 'file'
    input_file = sys.argv[1]

    #open file
    file_data = open(input_file, "r")

    #write context of the file in 'data'
    data = file_data.read()
    file_data.close()


    #user can decide weather he wants to encrypt or decrypt
    action = input("E: encrypt\nD: decrypt\n")
    
    if action.lower() == "e":

        output_file = input("Please type in the path to your output file!\
If the file does not exist, it is going to be\
created!\n")
        
        print("{} is going to be encrypted!".format(input_file))
        encrypt(data, output_file)
        print("{} has been encrypted! Your key is in a seperate file!\n".format(input_file))
        
    elif action.lower() == "d":

        key_file = input("Please provide the path to your key file!\n")

        key_file = open(key_file, "r")

        key = key_file.read()
        key_file.close()

        decrypt(data, key)
