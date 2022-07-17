'''Modules for terminal menu and screen clear.'''
import os
from simple_term_menu import TerminalMenu
from dog import Dog
import dogs_sql





def menu():
    '''Loops through menu until quit.'''
    options = ["Add Dog", "Delete Dog", "Get Info", "Feeding/Meds", "Grooming/Belongings", "Quit"]
    main_menu = TerminalMenu(options)
    info_options = ["All", "Large", "Small", "Search Name"]
    info_menu = TerminalMenu(info_options)

    quit = False

    while quit is False:
        options_list = main_menu.show()
        options_choice = options[options_list]

        if options_choice == "Quit":
            quit = True

        if options_choice == "Add Dog":
            name = input("Dog's name: ")
            owner = input("Owner's name: ")
            breed = input("Breed: ")
            while True:
                size = input("Large or Small: ")
                if size not in ("Large", "Small"):
                    print("Please enter Large or Small")
                else:
                    break
            while True:
                try:
                    age = int(input("Age: "))
                except ValueError:
                    print("Please enter a number")
                else:
                    break
            gender = input("Gender: ")
            feed_meds = input("Medication or special food required: ")
            grooming = input("Do they need grooming?: ")
            belongings = input("Do they have any belongings?: ")
            friendly = input("Are they friendly?: ")
            dog = Dog(name, owner, breed, size, age, gender,
                    feed_meds, grooming, belongings, friendly)
            dogs_sql.add_dog(dog)

        if options_choice == "Delete Dog":
            name = input("Name: ")
            dogs_sql.delete_dog(name)

        if options_choice == "Get Info":
            options_list = info_menu.show()
            options_choice = info_options[options_list]
            if options_choice == "All":
                print(dogs_sql.get_dogs())
            if options_choice == "Large":
                print(dogs_sql.get_large_dogs())
            if options_choice == "Small":
                print(dogs_sql.get_small_dogs())
            if options_choice == "Search Name":
                name = input("Name: ")
                print(dogs_sql.get_info(name))

        if options_choice == "Feeding/Meds":
            print(dogs_sql.feed_meds())

        if options_choice == "Grooming/Belongings":
            print(dogs_sql.out_groom())
            print(dogs_sql.out_belongings())

        else:
            print(options_choice)

    os.system("clear")

menu()
