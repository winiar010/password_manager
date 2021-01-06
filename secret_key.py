from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

#Utworzenie klucza kodującego base64
# def create_key():
#     password_provided = input("Podaj klucz kodujący:\n> ") 
#     password = password_provided.encode()  # konwert z typu bytes do utf-8
#     salt = os.urandom(16)  
#     kdf = PBKDF2HMAC(
#         algorithm=hashes.SHA256(),
#         length=32,
#         salt=salt,
#         iterations=100000,
#         backend=default_backend()
#     )
#     key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
#     with open("secret.key", "wb") as key_file:
#         key_file.write(key)

# create_key()

def load_key():
    return open("secret.key", "rb").read()

def encode_password():
    key = load_key()
    f = Fernet(key)
    print('Podaj hasło, które chcesz zakodować: ')
    simple_passwd = input("> ")
    simple_passwd = bytes(simple_passwd, encoding="utf-8")
    passw = f.encrypt(simple_passwd)
    return passw
    
# encode_password()

def decode_password(passw_to_decode):
    key = load_key()
    f = Fernet(key)
    passw_to_decode = bytes(passw_to_decode, encoding="utf-8")
    decoded_passwd = f.decrypt(passw_to_decode)
    return decoded_passwd

# decode_password()


# Create table
# conn = sqlite3.connect('admins.db')
# c = conn.cursor()
# c.execute("CREATE TABLE admins (
# 	"username"	VARCHAR,
# 	"password"	VARCHAR
# )")
# conn.close()

# conn = sqlite3.connect('accounts.db')
# c = conn.cursor()
# username = 'root'
# passw = encode_password()
# passw = str(passw, 'utf-8')
# c.execute("INSERT INTO admins (username, password) VALUES (?, ?)", (username, passw))
# conn.commit()
# conn.close()
