'''Modules for terminal menu and screen clear.'''
import os
from simple_term_menu import TerminalMenu
from dog import Dog
import dogsSDK



os.system("clear")

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
            size = input("Large or Small: ")
            age = input("Age: ")
            gender = input("Gender: ")
            feed_meds = input("Medication or special food required: ")
            grooming = input("Do they need grooming?: ")
            belongings = input("Do they have any belongings?: ")
            friendly = input("Are they friendly?: ")
            dog = Dog(name, owner, breed, size, age, gender,
                    feed_meds, grooming, belongings, friendly)
            dogsSDK.add_dog(dog)

        if options_choice == "Delete Dog":
            name = input("Name: ")
            dogsSDK.delete_dog(name)

        if options_choice == "Get Info":
            options_list = info_menu.show()
            options_choice = info_options[options_list]
            if options_choice == "All":
                print(dogsSDK.get_dogs())
            if options_choice == "Large":
                print(dogsSDK.get_large_dogs())
            if options_choice == "Small":
                print(dogsSDK.get_small_dogs())
            if options_choice == "Search Name":
                name = input("Name: ")
                print(dogsSDK.get_info(name))

        if options_choice == "Feeding/Meds":
            print(dogsSDK.feed_meds())

        if options_choice == "Grooming/Belongings":
            print(dogsSDK.out_groom())
            print(dogsSDK.out_belongings())

        else:
            print(options_choice)

menu()
