from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

# Utworzenie klucza kodującego base64
# def generate_key():
#     key = Fernet.generate_key()
#     with open("secret.key", "wb") as key_file:
#         key_file.write(key)

# generate_key()

# file = open('secret.key', 'rb')  # Open the file as wb to read bytes
# key = file.read()  # The key will be type bytes
# key.decode()
# print(key)
# file.close()

# password_provided = input("Podaj hasło kodujące:\n> ") 
# password = password_provided.encode()  # konwert z typu bytes do utf-8
# salt = os.urandom(16)  
# kdf = PBKDF2HMAC(
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=salt,
#     iterations=100000,
#     backend=default_backend()
# )
# key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
# print(key)

# def make_password():
#     file = open('secret.key', 'rb')
#     key = file.read()
#     print(key)
#     f = Fernet(key)
#     simple_passw = b'Maslo'
#     simple_passwd = f.encrypt(simple_passw)
    
#     print(simple_passw)
#     print('-'*40)

#     passwd = f.decrypt(simple_passwd)
#     print(passwd)
#     file.close()
# make_password()

password_provided = "Maslo" 
password = password_provided.encode()  # konwert z typu bytes do utf-8
salt = os.urandom(16)  
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
print(key)

f = Fernet(key)
simple_passw = b'Edukacja'
simple_passw = f.encrypt(simple_passw)
print(simple_passw)
print('-'*40)

passwd = f.decrypt(simple_passw)
print(passwd)











