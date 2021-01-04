def load_key():
#     """
#     Load the previously generated key
#     """
#     return open("secret.key", "rb").read()

# def encrypt_message(message):
#     """
#     Encrypts a message
#     """
#     key = load_key()
#     encoded_message = message.encode()
#     f = Fernet(key)
#     encrypted_message = f.encrypt(encoded_message)

#     print(encrypted_message)

# if __name__ == "__main__":
#     encrypt_message("encrypt this message")
