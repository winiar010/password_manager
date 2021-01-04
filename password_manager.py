from menu import menu, create, find, find_accounts
from getpass import getpass
import sys
import time

# menu
# 1. Create new password for a site
# 2. Find password for a site
# 3. Find all sites connected to an email
# 4. Change password

# secret = get_secret_key()         
SECRET_KEY = '123'

# passw = input('Wpisz hasło główne, aby użyć narzędzia: ')

time.sleep(1)

i = 0

while i < 3 :
    passw = getpass(prompt='Wpisz hasło główne, aby użyć narzędzia: \n> ')
    if passw == SECRET_KEY:
        print('Zalogowano poprawnie')
        break
    elif i == 2:
        print('Dostęp zablokowany')
        exit()
    else:
        print('No nie bardzo. Błędne hasło.')
        i += 1
        continue

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
        if choice not in ('1', '2', '3', 'Q', 'q', 'exit'):
            print('Wprowadź poprawny znak: ')
            continue
        if choice == 'Q' or 'q' or 'exit':
            exit()
    

         