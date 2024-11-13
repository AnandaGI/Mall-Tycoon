"""
Creator:    Ananda Irwin
Purpose:    Driver file for the tycoon game.
Updated:    10/14/2024
"""
from mall_functions import *
from store import *
from mall import Mall
import time, os

run_program = True

#Beginning of Program - Get the Mall Name
save_dir = os.path.dirname(os.path.realpath(__file__)) + "/saves/"
saves = os.listdir(save_dir)

if len(saves) != 0 and validate_yn("Would you like to load a save first?") == "Y":  #If there are no saves, don't bother loading
    print("\nThe following saves are available to load from:")
    i = 1
    for save in saves:
        print(str(i) + ")\t" + save.replace(".json", ""))
        i += 1
    user_index = validate_bounds("Please type the number of the save you wish to load.",
                                 1, len(saves))

    save_dest = save_dir + saves[user_index - 1]
    user_mall = load_mall(save_dest)
    input("Save loaded successfully. Press Enter to begin.")

else:
    print("\nWelcome to your very own Mall Planner! Add stores, items, and more!")
    user_mall = Mall(input("\nFirst, let's start off with a name! It needs to be something catchy.\t"))
    print("\nHmm.", end = "")

    for i in range(0, 3):
        time.sleep(0.75)
        print(".", end = "")

    input("\n\n" + user_mall.name + ", eh? That sounds great! Press ENTER to begin.")

#Main Program Loop
while run_program:

    #ADD A SIMULATE DAY FUNCTION
    print("\nActions:")
    print("1)\tCreate New Plot \n2)\tEdit Existing Plot \n3)\tCreate New Items\n4)\tRecall Product\n5)\tLoad Data From File")
    print("6)\tSave Data To File\n7)\tDisplay Mall Data \n8)\tExit Program")
    user_option = validate_bounds("Invalid choice. Must type a number", 1, 8)

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
            try:
                plot_sqr_feet = int(input("How large is your plot in square feet? Enter an integer:\t"))
            except:
                plot_sqr_feet = 0
                while plot_sqr_feet <= 0:
                    try:
                        plot_sqr_feet = int(input("Invalid choice. Must type a positive integer:\t"))
                    except:
                        pass
            print("Store type: \n1)\tRetail/Service store \n2)\tRestaurant \n3)\tMall department \n4)\tPlot")
            plot_type = validate_bounds("Type your plot's type", 1, 4)

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
                case _:
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

            user_mall.display_numbered_plots()
            store_choice = validate_bounds("Which store would you like to edit?",
                                           1, user_mall.num_stores)

            active_store = user_mall.get_store(store_choice-1)
            print("\nNow editing " + active_store.name + ".")

            print("Options: \n1)\tRebrand \n2)\tEdit Description \n3)\tEdit Items/Services \n4)\tDemolish Current Plot")
            store_option = validate_bounds("Enter option", 1, 4)

            #Go through options for store
            match store_option:
                case 1:     #Replace name of store
                    new_name = input("Please input a new name for " + active_store.name + ":\t")
                    active_store.name = new_name

                case 2:     #Replace description of store
                    new_description = input("Please input a new description for " + active_store.name + ":\t")
                    active_store.description = new_description

                case 3:     #Edit items.
                    if user_mall.num_items == 0:
                        print("No products to edit. To add products, first create them (Option 3 in Menu).")
                        continue
                    elif active_store.__class__.__name__ == "Plot":
                        print("Plots do not have any products to edit.")
                        continue

                    print("\nActions: \n1)\tAdd Product \n2)\tRemove Product \n3)\tEdit Product")
                    product_option = validate_bounds("Enter option", 1, 3)

                    match product_option:
                        #Add Product
                        case 1:
                            user_mall.display_products()
                            while True:
                                user_choice = validate_bounds("Add a product from the above list",
                                                              0, user_mall.num_items, zero_exit=True)
                                if user_choice == 0:
                                    break
                                else:
                                    new_product = copy_product( user_mall.get_item(user_choice-1) )
                                    active_store.add_product(new_product)  #Will add the product to the store

                            print("\nNew Store Catalog is:", end="")
                            active_store.display_catalog()

                        #Remove Product
                        case 2:
                            print("Select a product from the following list to remove:")
                            active_store.display_catalog()
                            index = validate_bounds("Type the number of the product you wish to remove:",
                                                          1, user_mall.num_items)

                            active_store.remove_product(active_store.get_product(index-1))

                        #Edit Product
                        case 3:
                            print("Select a product from the following list to edit:")
                            active_store.display_catalog()
                            user_choice = validate_bounds("Type the number of the product",
                                                          1, active_store.num_products)

                            store_product = active_store.get_product(user_choice-1)
                            store_product.print_stats()

                            print("\nWould you like to edit " + store_product.name + "'s" +
                                  "\n0)\tCancel \n1)\tPrice \n2)\tStock/Availability")
                            user_choice = validate_bounds("Type answer",
                                                          0, 2, zero_exit=True)

                            if user_choice == 1:
                                new_price = float(input("Please input a new price for " + store_product.name + ":\t"))
                                store_product.price = new_price

                            elif user_choice == 2:
                                if isinstance(store_product, Item):
                                    print("\nTo stock, input a positive amount. To destock, input a negative amount:\t")
                                    print(store_product.name + "'s current stock: " + str(store_product.stock) + "units")
                                    amount = int(input("Enter amount:\t" ))
                                    while amount < -store_product.stock:
                                        amount = int(input("Invalid amount. Enter a positive or negative integer:\t"))

                                    if amount >= 0:
                                        store_product.restock(amount)
                                    else:
                                        store_product.deplete_stock(-amount)

                                else:
                                    store_product.start = input(
                                        "What is the starting period your service is offered? (Format: XX:XX AM)\t")
                                    store_product.end = input(
                                        "What is the ending period your service is offered? (Format: XX:XX PM)\t")
                case 4:
                    user_mall.remove_plot(active_store)
            #End of Case 2


        #Create New Items
        #CASE 3, create new products for your stores/mall
        case 3:
            while True:
                new_product = create_product()
                user_mall.add_product(new_product)
                print(new_product.name + " has been successfully added.")

                if validate_yn("Would you like to add another product?") != "Y":
                    break
                #End of Case 3


        #Recall Products
        #Case 4, recall products and remove them from all stores
        case 4:
            if user_mall.num_items == 0:
                print("No products to recall.")
                continue

            user_mall.display_products()
            index = validate_bounds("Type the number of the product you wish to recall:",
                                    1, user_mall.num_items)

            user_mall.recall_product( user_mall.get_item(index-1) )
            #End of Case 4


        #Load Data From File
        #CASE 5, load data from a set of previously saved text files
        case 5:
            save_dir = os.path.dirname(os.path.realpath(__file__)) + "/saves/"
            saves = os.listdir(save_dir)
            if len(saves) == 0:
                print("\nThere are no previous saves to load from. (You may need to insert your memory card.)")
                continue    #Note: No memory card exists. This is a callback to the days of 8mb memory cards.

            print("\nThe following saves are available to load from:")
            i = 1
            for save in saves:
                print(str(i) + ")\t" + save.replace(".json", ""))
                i += 1
            user_index = validate_bounds("Please type the number of the save you wish to load.",
                                         0, len(saves), zero_exit=True)

            if user_index == 0:    #If the user wants to exit, skip the rest of the function
                continue

            save_dest = save_dir + saves[user_index-1]
            user_mall = load_mall(save_dest)
            #End of case 5


        #Save Data To File
        #CASE 6, save data to a set of new text files
        case 6:
            save_dest = save_dir + "/saves/" + input("\nWhat would you like to call your save?\t") + ".json"
            if os.path.exists(save_dest):
                if validate_yn("Save with this name already exists. Would you like to overwrite?") == "N":
                    continue

            save_mall(save_dest, user_mall)
            print("Data Saved Successfully.")
        #End of case 6


        #Display Stores
        #CASE 7, the user views all plots inside their mall
        case 7:

            print("\nDisplay Options: \n1)\tShorthand \n2)\tAll plot info \n3)\tSpecific Store Info" +
                  "\n4)\tMall Statistics \n5)\tASCII Representation", end="")
            user_choice = validate_bounds("Enter option", 1, 5)

            if user_choice != 4 and user_mall.num_stores == 0:  #If the user wants to display store info
                print("\nThere are no stores to display.")
                continue

            match user_choice:
                case 1:
                    user_mall.display_mall()
                case 2:
                    user_mall.display_all_plots()
                case 3:
                    user_mall.display_numbered_plots()
                    store_choice = validate_bounds("Which store would you like to see?",
                                                   1, user_mall.num_stores)
                    user_mall.get_store(store_choice-1).display_catalog()
                case 4:
                    print("\nMall Statistics:")
                    print("Stores:\t " + str(user_mall.num_stores))
                    print("Items:\t" + str(user_mall.num_items))
                    total_area = 0
                    for plot in user_mall.plot_list:
                        total_area += plot.square_feet
                    print("Combined area of stores:\t" + str(total_area) + " square feet")
                    print("Recalled items:\t" + str(user_mall.recalls))
                case 5:
                    print_mall(user_mall)
            print()     #Newline
            #End of Case 7


        #End the Program
        #CASE 8, the program boolean is set to false, stops program loop
        case 8:
            run_program = False
            if validate_yn("Would you like to save before closing the mall?") == "Y":
                curr_dir = os.path.dirname(os.path.realpath(__file__))
                save_dest = curr_dir + "/saves/" + input("What would you like to call your save?\t") + ".json"
                if os.path.exists(save_dest):
                    if validate_yn("Save with this name already exists. Would you like to overwrite?") == "N":
                        continue

                save_mall(save_dest, user_mall)
                print("Data Saved Successfully.")
            #End of Case 8

    #Stop before continuing with program loop
    if run_program:
        input("Press ENTER to continue.")

print("\n\nGoodbye!")