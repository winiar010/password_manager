from database_manager import store_passwords, master_key, find_users, find_password, delete_record
from datetime import datetime
from secret_key import encode_password, load_key, decode_password
from getpass import getpass

def menu():
    print('\r\n'*2 +'-'*40)
    print(('-'*17 + ' ') + 'Menu' + (' ' + '-'*17))
    print('1. Utwórz nowe hasło')
    print('2. Znajdź dane powiązane z adresem email')
    print('3. Znajdź hasło dla aplikacji lub strony')
    print('4. Usuń rekordy z bazy')
    print('Q Wyjście')
    # print('-h help')

def master():
    i = 0
    while i < 3:
        username = input("Login:\n> ")
        password = getpass(prompt='Wpisz hasło główne, aby użyć narzędzia: \n> ')
        
        decoded_passwd = master_key(username)

        if password == decoded_passwd:
            print('Zalogowano poprawnie')
            break
        elif i == 2:
            print('Dostęp zablokowany')
            exit()
        else:
            print('No nie bardzo. Błędne hasło.')
            i += 1
            continue

def create():
    print('Podaj nazwę aplikacji dla której chcesz zapisać hasło: ')
    app_name = input("> ")
    passw_to_encode = encode_password()
    passw_to_encode = str(passw_to_encode, 'utf-8')
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
    store_passwords(passw_to_encode, user_email, username, app_name, creation_time)

def find_accounts():
    user_email = input('Podaj adres email dla którego chcesz znaleźć zapisane konto:\n> ')
    find_users(user_email)

def find():
    app_name = input('Podaj nazwę strony www/aplikacji dla której chcesz znaleźć hasło:\n> ')
    find_password(app_name)

def delete():
    app_name = input('Podaj nazwę strony www/aplikacji, którą chcesz usunąć z bazy:\n> ')
    username = input('Podaj nazwę użytkownika strony www/aplikacji:\n> ')
    delete_record(app_name, username)