import sqlite3
from secret_key import decode_password
import subprocess


# Create table
# conn = sqlite3.connect('accounts.db')
# c = conn.cursor()
# c.execute("CREATE TABLE IF NOT EXISTS accounts (
#     password VARCHAR(255),
#     user_email VARCHAR(255),
#     username VARCHAR(255),
#     url VARCHAR(255),
#     app_name VARCHAR(255)
# )")
# conn.close()
# conn = sqlite3.connect('accounts.db')
# c = conn.cursor()
# c.execute("INSERT INTO accounts VALUES ('123','mw@wp.pl','mw010','facebook') ")
# conn.commit()
# conn.close()

def Extract3(result): 
            return [item[3] for item in result] 

def Extract1(result): 
            return [item[1] for item in result] 

def Extract0(result): 
            return [item[0] for item in result] 

# master key
def master_key(username):
    try:
        conn = sqlite3.connect('accounts.db')
        c = conn.cursor()
        result = c.execute("SELECT username, password FROM admins WHERE username = " + "\'" + username + "\'")
        result = c.fetchall()
        conn.commit()
        
        username = Extract0(result)
        passw_to_decode = Extract1(result)
        passw_to_decode = ''.join(passw_to_decode)
        decoded_passwd = decode_password(passw_to_decode)
        decoded_passwd = str(decoded_passwd, 'utf-8')
        return decoded_passwd
        conn.close()
        
    except sqlite3.Error as err:
        print(err)
        conn.close()

def store_passwords(passw, user_email, username, app_name, creation_time):
    try:
        conn = sqlite3.connect('accounts.db')
        c = conn.cursor()
        c.execute("INSERT INTO accounts (password, user_email, username, app_name, creation_time) VALUES (?,?,?,?,?)", (passw, user_email, username, app_name, creation_time)) #%s, %s, %s, %s
        conn.commit()
        print('Dane zostały poprawnie zapisane')
        conn.close()
    except sqlite3.Error as err:
        print(err)
        conn.close()

def find_users(user_email):
    data = ( 'Nazwa www/aplikacji: ','Email: ', 'Username: ', 'Password: ') 
    try:
        conn = sqlite3.connect('accounts.db')
        c = conn.cursor()
        result = c.execute("SELECT app_name, user_email, username, password FROM accounts WHERE user_email = " + "\'" + user_email + "\'")
        result = c.fetchall()
        conn.commit()
        
        passw_to_decode = Extract3(result)
        passw_to_decode = ''.join(passw_to_decode)
        decoded_passwd = decode_password(passw_to_decode)
        decoded_passwd = str(decoded_passwd, 'utf-8')

        if result is None:
            print('Nie ma danych dla podanego użytkownika')
        else:
            print('')
            print('Wyniki:')
            print('')
            for row in result:
                    for i in range(0, len(row)):
                        if data[i] == 'Password: ':
                            print(data[3] + decoded_passwd)
                        else:
                            print(data[i] + row[i])
            print('')
            print('-'*40)

        print("\nHasło zostało skopiowane do schowka!")
        subprocess.run('clip.exe', universal_newlines=True, input=decoded_passwd, shell=True)

        conn.close()

    except sqlite3.Error as err:
        print(err)
        conn.close()

def find_password(app_name):
    data = ( 'Username: ', 'Password: ')
    try:
        conn = sqlite3.connect('accounts.db')
        c = conn.cursor()
        result = c.execute("SELECT username, password FROM accounts WHERE app_name = " + "\'" + app_name + "\'")
        result = c.fetchall()
        conn.commit()

        passw_to_decode = Extract1(result)
        passw_to_decode = ''.join(passw_to_decode)
        decoded_passwd = decode_password(passw_to_decode)
        decoded_passwd = str(decoded_passwd, 'utf-8')
        
        if result is None:
            print('Nie ma danych dla podanego użytkownika')
        else:
            print('')
            print('Wyniki:')
            print('')
            for row in result:
                    for i in range(0, len(row)):
                        if data[i] == 'Password: ':
                            print(data[1] + decoded_passwd)
                        else:
                            print(data[i] + row[i])
            print('')
            print('-'*40)

        print("\nHasło zostało skopiowane do schowka!")
        subprocess.run('clip.exe', universal_newlines=True, input=decoded_passwd, shell=True)

        conn.close()

    except sqlite3.Error as err:
        print(err)
        conn.close()

def delete_record(app_name, username):
    try:
        conn = sqlite3.connect('accounts.db')
        c = conn.cursor()
        result = c.execute("DELETE FROM accounts WHERE app_name = " + "\'" + app_name + "\'" + "AND username = " + "\'" + username + "\'")
        result = c.fetchall()
        conn.commit()

        print("\nDane dla usera: "+ username +" i aplikacji "+ app_name +" zostały poprawnie usunięte z bazy.")  

        conn.close()    
    except sqlite3.Error as err:
        print(err)
        conn.close()