from menu import menu, master, create, find, find_accounts, delete
import sys
import time
from secret_key import load_key, encode_password, decode_password
from database_manager import master_key

# menu
# 1. Create new password for a site
# 2. Find password for a site
# 3. Find all sites connected to an email
# 4. Delete records
       
# secret_key = master_key()

time.sleep(1)

master()

while True:
    menu()
    choice = None
    while True:
        choice = input("> ")    
        if choice == '1':
            create()
            break
        if choice == '2':
            find_accounts()
            break
        if choice == '3':
            find()
            break
        if choice == '4':
            delete()
            break
        if choice not in ('1', '2', '3', '4', 'Q', 'q', 'exit'):
            print('Wprowadź poprawny znak: ')
            continue
        if choice == 'Q' or 'q' or 'exit':
            exit()
    

         