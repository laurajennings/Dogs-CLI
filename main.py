import os
os.system("clear")
from simple_term_menu import TerminalMenu 
from dog import Dog
import dogsSDK


#dog1 = Dog("Hades", "large")
#print(dogsSDK.add_dog(dog1))
#print(dogsSDK.get_dogs())
#print(dogsSDK.get_info("Hades"))



def main_menu():
    options = ["Add Dog", "Delete Dog", "Get Info", "Incoming", "Feeding/Meds", "Outgoing", "Quit"]
    main_menu = TerminalMenu(options)

    quit = False

    while quit == False:
        optionsList = main_menu.show()
        optionsChoice = options[optionsList]

        if(optionsChoice == "Quit"):
            quit = True
        if(optionsChoice == "Add Dog"):
            name = input("Dog's name: ")
            size = input("Large or Small?: ")
            dog = Dog(name, size)
            dogsSDK.add_dog(dog)
        if(optionsChoice == "Delete Dog"):
            dogsSDK.delete_dog("Hades")

        if(optionsChoice == "Get Info"):
            print(dogsSDK.get_dogs())
        if(optionsChoice == "Incoming"):
            print("income")
        if(optionsChoice == "Feeding/Meds"):
            print("feed")
        if(optionsChoice == "Outgoing"):
            print("out")
        else:
            print(optionsChoice)

main_menu()