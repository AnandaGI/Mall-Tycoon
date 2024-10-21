"""
Creator:    Ananda Irwin
Purpose:    Driver file for the tycoon game.
Updated:    10/14/2024
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

input("\n\n" + str(user_mall) + ", eh? That sounds great! Press ENTER to begin.")

#Main Program Loop
while run_program:

    print("\nActions:")
    print("1)\tCreate New Store \n2)\tEdit Existing Store \n3)\tCreate New Items\n4)\tMall Actions\n5)\tLoad Data From File")
    print("6)\tSave Data To File\n7)\tDisplay Stores \n8)\tExit Program")
    user_option = int(input("Choose option 1-8:\t"))
    while user_option < 1 or user_option > 8:
        user_option = int(input("Invalid choice. Must type a number 1-8:\t"))

    """
    Execute Different Actions
    """
    match user_option:
        #Case 1, The user will add a new store to the mall.
        case 1:
            #Gain input for the name, description, and type of store.
            store_name = input("\nWhat is your new store's name?\t")
            store_description = input("Give a short description of your store:\t")
            store_sqr_feet = int(input("How large is your store in square feet? Enter an integer:\t"))
            store_type = int(input("Is your store a (1)retail/service store, (2)restaurant, (3)mall department?\t"))
            while store_type < 1 or store_type > 3:
                store_type = int(input("\nInvalid option. Which of the above best describes your store? (enter the #)\t"))

            #Create the new store
            match store_type:
                case 1:
                    new_store = Store(store_name, store_description, store_sqr_feet)
                case 2:
                    new_store = Restaurant(store_name, store_description, store_sqr_feet)
                case 3:
                    new_store = Department(store_name, store_description, store_sqr_feet)

            user_mall.add_store(new_store)  #Add new store to the mall
            print("\n" + str(new_store) + " has been successfully added to " + str(user_mall))
            input("Press ENTER to continue.")


        #Case 2, user will edit a store name, description, or manipulate the items within
        case 2:
            user_mall.display_store_list()
            store_choice = int(input("Which store would you like to edit?\t"))
            while store_choice < 1 or store_choice > user_mall.num_stores:
                store_choice = int(input("Invalid selection. Please select a store from the list above:\t"))

            active_store = user_mall.get_store(store_choice-1)
            print(("-"*20) + "\n" + str(active_store) + "\nDescription: " + active_store.get_description() + ("-"*20))

            print("Options: \n1)\tEdit Name \n2)\tEdit Description \n3)\tEdit Items/Services")
            store_option = int(input("Choose option 1-3:\t"))
            while store_option < 1 or store_option > 3:
                store_option = int(input("Invalid choice. Must type a number 1-3:\t"))

            #Go through options for store
            match store_option:
                case 1:     #Replace name of store
                    new_name = input("Please input a new name for " + str(active_store) + ":\t")
                    active_store.set_name(new_name)

                case 2:     #Replace description of store
                    new_description = input("Please input a new name for " + str(active_store) + ":\t")
                    active_store.set_description(new_description)

                case 3:     #Edit items.
                    print("\nActions: \n1)\tAdd Product \n2)\tRemove Product \n3)\tEdit Product Stock/TimeSlots")
                    product_option = int(input("Choose option 1-3:\t"))
                    while product_option < 1 or product_option > 3:
                        product_option = int(input("Invalid choice. Must type a number 1-3:\t"))

                    match product_option:
                        case 1:
                            user_mall.display_products()
                            user_choice = input("Add a product from the above list (1 - " + str(user_mall.num_items) + ") or create new product (0):\t")
                            while user_choice < 0 or user_choice > user_mall.num_items:
                                user_choice = int(input("Invalid choice. Must type a valid integer:\t"))

                            if user_choice == 0:
                                active_store.add_product(create_product())  #Adds a product to the store using the
                                                                            #create_product function in product.py
                            else:
                                new_product = copy_product(user_mall.get_item(user_choice))
                                active_store.add_product(new_product)

                            print("New Catalog is:")
                            active_store.display_catalog()

                        case 2:
                            pass
                            #Remove item

                        case 3:
                            pass
                            #Edit item


        case 3:
            pass
        case 4:
            pass

        case 5:
            user_mall.display_mall()
            input("\nPress ENTER to continue.")

        case 6:
            run_program = False



