import sqlite3
from dog import Dog

def cursor():
    return sqlite3.connect('dogs.db').cursor()

c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS dogs (name TEXT, owner TEXT, breed TEXT, size TEXT, age TEXT, gender TEXT, feed_meds TEXT, grooming TEXT, belongings TEXT, friendly TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS large (name TEXT, owner TEXT, breed TEXT, size TEXT, age TEXT, gender TEXT, feed_meds TEXT, grooming TEXT, belongings TEXT, friendly TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS small (name TEXT, owner TEXT, breed TEXT, size TEXT, age TEXT, gender TEXT, feed_meds TEXT, grooming TEXT, belongings TEXT, friendly TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS groom (name TEXT, owner TEXT, breed TEXT, size TEXT, age TEXT, gender TEXT, feed_meds TEXT, grooming TEXT, belongings TEXT, friendly TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS feed_meds (name TEXT, owner TEXT, breed TEXT, size TEXT, age TEXT, gender TEXT, feed_meds TEXT, grooming TEXT, belongings TEXT, friendly TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS belongings (name TEXT, owner TEXT, breed TEXT, size TEXT, age TEXT, gender TEXT, feed_meds TEXT, grooming TEXT, belongings TEXT, friendly TEXT)')
c.connection.close()

def add_dog(dog):
    c = cursor()
    with c.connection:
        c.execute("INSERT INTO dogs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (dog.name, dog.owner, dog.breed, dog.size, dog.age, dog.gender, dog.feed_meds, dog.grooming, dog.belongings, dog.friendly))
        c.execute("INSERT INTO belongings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (dog.name, dog.owner, dog.breed, dog.size, dog.age, dog.gender, dog.feed_meds, dog.grooming, dog.belongings, dog.friendly))
        if dog.size == "Large":
            c.execute("INSERT INTO large VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (dog.name, dog.owner, dog.breed, dog.size, dog.age, dog.gender, dog.feed_meds, dog.grooming, dog.belongings, dog.friendly))
        if dog.size == "Small":
            c.execute("INSERT INTO small VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (dog.name, dog.owner, dog.breed, dog.size, dog.age, dog.gender, dog.feed_meds, dog.grooming, dog.belongings, dog.friendly))
        if dog.grooming == "Yes":
            c.execute("INSERT INTO groom VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (dog.name, dog.owner, dog.breed, dog.size, dog.age, dog.gender, dog.feed_meds, dog.grooming, dog.belongings, dog.friendly))

    c.connection.close()
    

# def add_large(dog):
#     c = cursor()
#     with c.connection:
#         c.execute("INSERT INTO large VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (dog.name, dog.owner, dog.breed, dog.size, dog.age, dog.gender, dog.feed_meds, dog.grooming, dog.belongings, dog.friendly))
#     c.connection.close()

# def add_small(dog):
#     c = cursor()
#     with c.connection:
#         c.execute("INSERT INTO small VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (dog.name, dog.owner, dog.breed, dog.size, dog.age, dog.gender, dog.feed_meds, dog.grooming, dog.belongings, dog.friendly))
#     c.connection.close()
    
def get_dogs():
    c = cursor()
    dogs = []
    with c.connection:
        for dog in c.execute('SELECT * FROM dogs'):
            dogs.append(Dog(dog[0], dog[1], dog[2], dog[3], dog[4], dog[5], dog[6], dog[7], dog[8], dog[9]))
    c.connection.close()
    return dogs

def get_large_dogs():
    c = cursor()
    large = []
    with c.connection:
        for dog in c.execute('SELECT * FROM large'):
            large.append(Dog(dog[0], dog[1], dog[2], dog[3], dog[4], dog[5], dog[6], dog[7], dog[8], dog[9]))
    c.connection.close()
    return large

def get_small_dogs():
    c = cursor()
    small = []
    with c.connection:
        for dog in c.execute('SELECT * FROM small'):
            small.append(Dog(dog[0], dog[1], dog[2], dog[3], dog[4], dog[5], dog[6], dog[7], dog[8], dog[9]))
    c.connection.close()
    return small

def get_info(name):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM dogs WHERE name=?', (name,))
    dog =  c.fetchone()
    c.connection.close()
    if not dog:
        return None
    return Dog(dog[0], dog[1], dog[2], dog[3], dog[4], dog[5], dog[6], dog[7], dog[8], dog[9])

def delete_dog(name):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM dogs WHERE name=?', (name,))
        c.execute('DELETE FROM large WHERE name=?', (name,))
        c.execute('DELETE FROM small WHERE name=?', (name,))
        c.execute('DELETE FROM groom WHERE name=?', (name,))
        c.execute('DELETE FROM feed_meds WHERE name=?', (name,))
        c.execute('DELETE FROM belongings WHERE name=?', (name,))
    c.connection.close()

def out_groom():
    c = cursor()
    with c.connection:
        c.execute('SELECT name FROM groom')
        dog = c.fetchall() 
        print("Dogs to groom:")
        print(dog)
    c.connection.close()

def out_belongings():
    c = cursor()
    with c.connection:
        c.execute('SELECT name, belongings FROM belongings')
        dog = c.fetchall() 
        print("Belongings:")
        print(dog)
    c.connection.close()

# def get_dogs():
#     c = cursor()
#     with c.connection:
#         c.execute('SELECT * FROM dogs')
#     return c.fetchall()
