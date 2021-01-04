from hash_maker import password
import subprocess
from database_manager import store_passwords, find_users, find_password
from datetime import datetime

def menu():
    print('\r\n'*2 +'-'*40)
    print(('-'*17 + ' ') + 'Menu' + (' ' + '-'*17))
    print('1. Utwórz nowe hasło')
    print('2. Znajdź dane powiązane z adresem email')
    print('3. Znajdź hasło dla aplikacji lub strony')
    print('Q Wyjście')
    # print('-h help')

def create():
    print('Podaj nazwę aplikacji dla której chcesz zapisać hasło: ')
    app_name = input("> ")
    print('Podaj hasło, które chcesz zakodować: ')
    simple_passwd = input("> ")
    passw = password(simple_passwd, app_name, 12)
    subprocess.run('clip.exe', universal_newlines=True, input=passw, shell=True)
    print('-'*30)
    print('')
    print('Twoje hasło zostało utworzone i skopiowane do schowka: ')
    print('')
    print('-' *30)
    user_email = input('Podaj email użytkownika strony www/aplikacji:\n> ')
    username = input('Podaj nazwę użytkownika strony www/aplikacji:\n> ')
    if username == None:
        username = ''
    creation_time = datetime.now()
    creation_time = (creation_time.strftime("%Y-%m-%d %H:%M:%S"))
    store_passwords(passw, user_email, username, app_name, creation_time)

def find():
    app_name = input('Podaj nazwę strony www/aplikacji dla której chcesz znaleźć hasło:\n> ')
    find_password(app_name)

def find_accounts():
    user_email = input('Podaj adres email dla którego chcesz znaleźć zapisane konto:\n> ')
    find_users(user_email)

