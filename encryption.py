from cryptography.fernet import Fernet

def key_generate():

    
    key = Fernet.generate_key()

    output_file = open("key.txt", "wb")
    output_file.write(key)
    output_file.close()

    return key


#encryption of data in file
def encrypt(files, key):
    #initialize key
    f = Fernet(key)

    for file in files:
        with open(file, "rb") as rfile:
            data = rfile.read()

        #encrypt data
        token = f.encrypt(data)

        #open/create the file
        f_file = open(file, "wb")

        #write the file
        f_file.write(token)
        f_file.close



if __name__ == "__main__":
    
    key = key_generate()

    file = input("Type in the path to the file: ")

    encrypt(file, key)