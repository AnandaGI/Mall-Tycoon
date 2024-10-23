"""
Creator:    Ananda Irwin
Purpose:    Driver file for the tycoon game.
Updated:    10/14/2024
"""

from product import *
from store import *
from mall import Mall
import time
from pathlib import Path
import os

run_program = True

#Beginning of Program - Get the Mall Name
#print("\nWelcome to your very own Mall Planner! Add stores, items, and more!")
user_mall = Mall(input("\nFirst, let's start off with a name! It needs to be something catchy.\t"))
#print("\nHmm.", end = "")

#for i in range(0, 3):
    #time.sleep(0.75)
    #print(".", end = "")

#input("\n\n" + user_mall.name + ", eh? That sounds great! Press ENTER to begin.")

#Main Program Loop
while run_program:

    print("\nActions:")
    print("1)\tCreate New Plot \n2)\tEdit Existing Plot \n3)\tCreate New Items\n4)\tRecall Product\n5)\tLoad Data From File")
    print("6)\tSave Data To File\n7)\tDisplay Stores \n8)\tExit Program")
    user_option = int(input("Choose option 1-8:\t"))
    while user_option < 1 or user_option > 8:
        user_option = int(input("Invalid choice. Must type a number 1-8:\t"))

    """
    Execute Different Actions
    """
    match user_option:
        #Create New Plot
        #CASE 1, The user will add a new store to the mall.
        case 1:
            #Gain input for the name, description, and type of store.
            plot_name = input("\nWhat is your new plot's name?\t")
            plot_description = input("Give a short description of your plot:\t")
            plot_sqr_feet = int(input("How large is your plot in square feet? Enter an integer:\t"))
            plot_type = int(input("Store type: \n1)\tRetail/Service store \n2)\tRestaurant \n3)\tMall department? \n4)\tPlot\n"))
            while plot_type < 1 or plot_type > 4:
                plot_type = int(input("\nInvalid option. Which of the above best describes your store? (enter the #)\t"))

            #Create the new store
            match plot_type:
                case 1:
                    new_plot = Store(plot_name, plot_description, plot_sqr_feet)
                case 2:
                    num_seats = int(input("How many seats can you restaurant provide?\t"))
                    if num_seats != 0 and plot_sqr_feet / num_seats < 25:   #If bending the laws of time and space
                        print(num_seats, "for", plot_sqr_feet, "square feet? I'm sure it's bigger on the inside.")
                    new_plot = Restaurant(plot_name, plot_description, plot_sqr_feet, num_seats)
                case 3:
                    new_plot = Department(plot_name, plot_description, plot_sqr_feet)
                case 4:
                    new_plot = Plot(plot_name, plot_description, plot_sqr_feet)

            user_mall.add_store(new_plot)  #Add new store to the mall
            print("\n" + new_plot.name + " has been successfully added to " + user_mall.name)
            #End of Case 2


        #Edit Existing Plot
        #CASE 2, user will edit a store name, description, or manipulate the items within
        case 2:
            if user_mall.num_stores == 0:
                print("\nThere are no stores in your mall yet.")
                continue

            user_mall.display_store_list()
            store_choice = int(input("Which store would you like to edit?\t"))
            while store_choice < 1 or store_choice > user_mall.num_stores:
                store_choice = int(input("Invalid selection. Please select a store from the list above:\t"))

            active_store = user_mall.get_store(store_choice-1)
            print("\nNow editing " + active_store.name + ".")

            print("Options: \n1)\tEdit Name \n2)\tEdit Description \n3)\tEdit Items/Services")
            store_option = int(input("Choose option 1-3:\t"))
            while store_option < 1 or store_option > 3:
                store_option = int(input("Invalid choice. Must type a number 1-3:\t"))

            #Go through options for store
            match store_option:
                case 1:     #Replace name of store
                    new_name = input("Please input a new name for " + str(active_store) + ":\t")
                    active_store.name = new_name

                case 2:     #Replace description of store
                    new_description = input("Please input a new description for " + str(active_store) + ":\t")
                    active_store.description = new_description

                case 3:     #Edit items.
                    if user_mall.num_items == 0:
                        print("No products to edit. To add products, first create them (Option 3 in Menu).")
                        continue

                    print("\nActions: \n1)\tAdd Product \n2)\tRemove Product \n3)\tEdit Product Stock/TimeSlots")
                    product_option = int(input("Choose option 1-3:\t"))
                    while product_option < 1 or product_option > 3:
                        product_option = int(input("Invalid choice. Must type a number 1-3:\t"))

                    match product_option:
                        #Add Product
                        case 1:
                            print("\nActive Products: " + str([product.name for product in user_mall.active_products]))
                            if input("Add to your active products from saved? (Y or N)\t").upper() == "Y":
                                while True:
                                    user_mall.display_products()
                                    print("Add a product from the above list (1 - " + str(user_mall.num_items) + ")")
                                    user_choice = int(input("Or type 0 to exit.\t"))
                                    while user_choice < 0 or user_choice > user_mall.num_items:
                                        user_choice = int(input("Invalid choice. Must type a valid integer:\t"))

                                    if user_choice != 0:
                                        new_product = user_mall.get_item(user_choice-1)
                                        user_mall.add_product(new_product)  #Will append the product only to the active_list
                                    else:
                                        break

                                    print("\nActive Products: " + str([product.name for product in user_mall.active_products]))

                            for product in user_mall.active_products:
                                active_store.add_product(product)
                            print("\nNew Store Catalog is:")
                            active_store.display_catalog()

                            print("\nWould you like to keep your active products to add them to another store?")
                            print("Active Products: " + str([product.name for product in user_mall.active_products]))
                            if input("Type Y or N:\t").upper() != "Y":
                                user_mall.clear_products()

                        #Remove Product
                        case 2:
                            print("Select a product from the following list to remove:")
                            active_store.display_catalog()
                            user_choice = input("\nType the number of the product you wish to remove:\t")
                            while user_choice < 1 or user_choice > user_mall.num_items:
                                user_choice = int(input("Invalid choice. Must type a valid integer:\t"))

                            active_store.remove_product(user_choice-1)

                        #Edit Product
                        case 3:
                            print("Select a product from the following list to edit:")
                            active_store.display_catalog()
                            user_choice = int(input("Type the number of the product:\t"))
                            while user_choice < 1 or user_choice > user_mall.num_items:
                                user_choice = int(input("Invalid choice. Must type a valid integer:\t"))

                            store_product = active_store.get_product(user_choice)
                            store_product.print_stats()

                            print(
                                "\nWould you like to edit " + store_product.name + "'s \n0)\tCancel \n1)\tPrice \n2)\tStock/Availability")
                            user_choice = input()
                            while user_choice != 0 or 1 or 2:
                                user_choice = input("Not a valid option. Please type an integer 0 - 2:\t")

                            if user_choice == 1:
                                new_price = float(input("Please input a new price for " + store_product.name + ":\t"))
                                store_product.price = new_price

                            else:
                                if isinstance(store_product, Item):
                                    amount = int(input(
                                        "How much stock do you want to add or remove? (Type a positive or negative integer)\t"))
                                    if amount >= 0:
                                        store_product.restock(amount)
                                    else:
                                        store_product.deplete_stock(-amount)

                                else:
                                    store_product.start = input(
                                        "What is the starting period your service is offered? (Format: XX:XX AM)\t")
                                    store_product.end = input(
                                        "What is the ending period your service is offered? (Format: XX:XX PM)\t")
            #End of Case 2


        #Create New Items
        #CASE 3, create new products for your stores/mall
        case 3:
            while True:
                new_product = create_product()
                user_mall.add_product(new_product)

                print("\nNew list of active products: " + str([product.name for product in user_mall.active_products]))
                if input("Would you like to add another product? (Y or N) ").upper() != "Y":
                    break
                #End of Case 3


        #Recall Products
        #Case 4, recall products and remove them from all stores
        case 4:
            if user_mall.num_items == 0:
                print("No products to recall.")
                continue

            user_mall.display_products()
            index = int(input("\nType the number of the product you wish to recall:\t"))
            while index < 1 or index > user_mall.num_items:
                index = int(input("Invalid choice. Must type a valid integer:\t"))

            user_mall.recall_product( user_mall.get_item(index) )
            #End of Case 4


        #Load Data From File
        #CASE 5, load data from a set of previously saved text files
        case 5:
            pass


        #Save Data To File
        #CASE 6, save data to a set of new text files
        case 6:
            curr_dir = os.path.dirname(os.path.realpath(__file__))
            save_dest = curr_dir + "/saves/" + input("\nWhat would you like to call your save?\t") + ".txt"
            f = open(save_dest, "w")
            f.write(user_mall.name + "\n")

            for plot in user_mall.store_list:
                f.write(str(plot.__class__) + "\n" + plot.name + "\n" + plot.description + "\n")
                if plot.__class__ is Restaurant:
                    f.write(str(plot.seats) + "\n")

                # This returns FALSE if and only if plot IS a plot, since they have no items
                if not plot.__class__ is Plot:
                    f.write(str(plot.num_products) + "\n")
                    for product in plot.list:
                        f.write(str(product.__class__) + "\n" + product.name + "\n")
                        f.write(product.description + "\n" + str(product.price) + "\n")
                        if isinstance(product, Item):
                            f.write(str(product.stock) + "\n")
                        else:
                            f.write(product.start + "\n" + product.end + "\n")
                f.write("#\n")    #Delimiter, tells the loading part when to move on to a new store
            f.close()



        #Display Stores
        #CASE 7, the user views all plots inside their mall
        case 7:
            user_mall.display_mall()
            #End of Case 7


        #End the Program
        #CASE 8, the program boolean is set to false, stops program loop
        case 8:
            run_program = False
            print("Goodbye!")
            #End of Case 8

    #Stop before continuing with program loop
    if run_program:
        input("Press ENTER to continue.")


#This returns true if and only if the object is of the specified class excluding subclasses
def exact_instance(obj, class_type):
    return obj.__class__ is class_type