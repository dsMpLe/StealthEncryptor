#python encryptor which takes an input and encrypts it

#2024-05-10 - Dennis Ortlieb

import sys
from cryptography.fernet import Fernet

key = Fernet.generate_key()

if len(sys.argv) == 2:
    data = b(sys.argv[1])
    f = Fernet(key)
    token = f.encrypt(data)

    print(str(data))

    data = f.decrypt(token)

    print(str(data))