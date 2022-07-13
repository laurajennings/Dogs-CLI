# LauraJennings_T1A3
Terminal App
MAIN
from simple_term_menu import TerminalMenu 
import os
os.system("clear")
import sqlite3
from dog import Dog
import dogsSDK

dog = Dog("Hades", "Large")
print(dogsSDK.add_dog(dog))

print(dogsSDK.get_info(dog))

SDK
import sqlite3
from dog import Dog

def cursor():
    return sqlite3.connect('dogs.db').cursor()

c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS dogs (name TEXT, size TEXT)')
c.connection.close()

def add_dog(dog):
    c = cursor()
    c.execute('INSERT INTO dogs VALUES (?, ?', (dog.name, dog.size))
    c.connection.close()


def get_info(name):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM dogs WHERE name=?', (name,))
    data =  c.fetchone()
    if not data:
        return None
    return Dog(data[0], data[1])

DOG
class Dog():

    # large = []
    # small = []

    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    # def is_large(self):
    #     if self.size == "Large":
    #         Dog.large.append(dog)
    #     Dog.small.append(dog)

    def __str__(self):
        return f"{self.name}{self.size}"








class Dog(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{}'.format(self.name)

    def getName(self):
        self.name

class All_Dogs:
    def __init__(self):
        self.items=[]
    
    def add_items(self, newItem):
        self.items.append(newItem)


conn = sqlite3.connect(":memory:")

c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS dogs (name TEXT, breed TEXT)')

def add_dog():
    name = input("Dog's name: ")
    breed = input("Breed: ")
    c.execute('INSERT INTO dogs VALUES (name, breed)')
    conn.commit()

def get_info():
    c.exucute('SELECT * FROM books')