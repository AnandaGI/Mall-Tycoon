"""
Creator:    Ananda Irwin
Purpose:    Driver file for the tycoon game.
Updated:    10/13/2024
"""

from product import *
from store import *
from mall import Mall
import time

run_program = True

#Beginning of Program - Get the Mall Name
print("\nWelcome to your very own Mall Planner! Add stores, items, and more!")
mall_name = input("\nFirst, let's start off with a name! It needs to be something catchy.\t")
user_mall = Mall(mall_name)
print("\nHmm.", end = "")

for i in range(0, 3):
    time.sleep(0.75)
    print(".", end = "")

print("\n\n" + str(user_mall) + ", eh? That sounds great! Let's begin:")
time.sleep(2)

while run_program:

    print("\nActions:")
    print("1)\tCreate New Store\n2)\tEdit Existing Store\n3)\tLoad Data From File\n4)\tSave Data To File")
    print("5)\tDisplay Stores\n6)\tEnter User Perspective\n7)\tExit Program")
    user_option = int(input("Choose option 1-5:\t"))
    while user_option < 1 or user_option > 7:
        user_option = int(input("Invalid choice. Must type a number 1-6:\t"))

    match user_option:
        #Case 1, The user will add a new store to the mall.
        case 1:
            #Gain input for the name, description, and type of store.
            store_name = input("\nWhat is your new store's name?\t")
            store_description = input("Give a short description of your store:\t")
            store_type = int(input("Does your store sell goods (1), services (2), or both?(3)\t"))
            while store_type < 1 or store_type > 3:
                store_type = int(input("\nInvalid option. Does your store sell goods (1), services (2), or both?(3)\t"))

            #Create the new store
            match store_type:
                case 1:
                    new_store = RetailStore(store_name, store_description)
                case 2:
                    new_store = ServiceStore(store_name, store_description)
                case 3:
                    new_store = ComboStore(store_name, store_description)

            user_mall.add_store(new_store)  #Add new store to the mall
            print("\n" + str(new_store) + " has been successfully added to " + str(user_mall))
            input("Press ENTER to continue.")


        case 2:
            pass
        case 3:
            pass
        case 4:
            pass

        case 5:
            user_mall.display_mall()
            input("\nPress ENTER to continue.")

        case 6:
            pass
        case 7:
            run_program = False



