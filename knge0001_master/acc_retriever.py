import sqlite3


def get_account(email):
    conn = sqlite3.connect('testing.db')
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE email =(?)', (email,))
    data = c.fetchall()
    conn.close()
    return data


if __name__ == '__main__':
    print(get_account("test@gmail.com"))