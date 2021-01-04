import sqlite3

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
    data = ('Password: ', 'Email: ', 'Username:', 'App/Site name: ') 
    try:
        conn = sqlite3.connect('accounts.db')
        c = conn.cursor()
        result = c.execute("SELECT password, user_email, username, app_name FROM accounts WHERE user_email = " + "\'" + user_email + "\'")
        result = c.fetchall()
        conn.commit()
        
        if result is None:
            print('Nie ma danych dla podanego użytkownika')
        else:
            print('')
            print('Wyniki:')
            print('')
            for row in result:
                for i in range(0, len(row)-1):
                    print(data[i] + row[i])
            print('')
            print('-'*40)

    except sqlite3.Error as err:
        print(err)
        conn.close()

def find_password(app_name):
    try:
        conn = sqlite3.connect('accounts.db')
        c = conn.cursor()
        result = c.execute("SELECT password FROM accounts WHERE app_name = " + "\'" + app_name + "\'")
        conn.commit()
        result = c.fetchone()
        print('Hasło to: ' )
        print(result[0])
        conn.close()
    except sqlite3.Error as err:
        print(err)
        conn.close()
