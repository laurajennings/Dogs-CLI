import sqlite3
from dog import Dog

def cursor():
    return sqlite3.connect('dogs.db').cursor()

c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS dogs (name TEXT, size TEXT)')
c.connection.close()

def add_dog(dog1):
    c = cursor()
    with c.connection:
        c.execute("INSERT INTO dogs VALUES (?, ?)", (dog1.name, dog1.size))
    c.connection.close()
    return c.lastrowid
    
def get_dogs():
    c = cursor()
    dogs = []
    with c.connection:
        for dog1 in c.execute('SELECT * FROM dogs'):
            dogs.append(Dog(dog1[0], dog1[1]))
    c.connection.close()
    return dogs

def get_info(name):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM dogs WHERE name=?', (name,))
    data =  c.fetchone()
    c.connection.close()
    if not data:
        return None
    return Dog(data[0], data[1])

def delete_dog(name):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM dogs WHERE name=?', (name,))
    rows = c.rowcount
    c.connection.close()
    return rows


# def get_dogs():
#     c = cursor()
#     with c.connection:
#         c.execute('SELECT * FROM dogs')
#     return c.fetchall()
