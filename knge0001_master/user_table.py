import sqlite3


# DB Management Method
def create_usertable():
    conn = sqlite3.connect('testing.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(date DATE, name TEXT, number INTEGER, email TEXT PRIMARY KEY,password TEXT , logintimes INTEGER)')
    conn.close()


def add_userdata(date, name, number, email, password, logintimes):
    conn = sqlite3.connect('testing.db')
    c = conn.cursor()
    c.execute('INSERT INTO userstable(date, name, number, email,password,logintimes) VALUES (?,?,?,?,?,?)', (date, name, number, email,password,logintimes))
    conn.commit()
    conn.close()


def login_user(email, password):
    conn = sqlite3.connect('testing.db')
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE email =? AND password = ?', (email, password))
    data = c.fetchall()
    conn.close()
    return data


def view_all_users():
    conn = sqlite3.connect('testing.db')
    c = conn.cursor()
    c.execute('SELECT date,name,number,email,logintimes FROM userstable')
    data = c.fetchall()
    conn.close()
    return data


def update_login_count(email):
    """
    function to count and update the number of times user login based on the user email
    this function is only called when login is successfull
    """
    conn= sqlite3.connect('testing.db')
    c = conn.cursor()
    c.execute('UPDATE userstable SET logintimes= logintimes+1 WHERE email = ?',(email,))
    conn.commit()
    data= c.fetchall()
    conn.close()
    return data
