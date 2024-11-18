"""
Creator:    Ananda Irwin
Purpose:    Additional functions for the driver to improve readability.
Updated:    10/30/2024
"""

import json
from mall import Mall
from store import *
from product import *

#Validates that an integer is within a given range, looping until a valid integer can be returned
def validate_bounds(message: str, lower_bound: int, upper_bound: int, zero_exit=False):
    if zero_exit:
        message = "\n" + message + " (" + str(lower_bound+1) + " - " + str(upper_bound) + ")" + " (0 to exit)"
    else:
        message = "\n" + message + " (" + str(lower_bound) + " - " + str(upper_bound) + ")"

    try:
        answer = int(input(message + ":\t"))
        while answer < lower_bound or answer > upper_bound:
            answer = int(input("Invalid choice. Must type a number (" + str(lower_bound) + " - " + str(upper_bound) + "):\t"))
    except ValueError:
        answer = -1
        while answer < lower_bound or answer > upper_bound:
            try:
                answer = int(input("Invalid choice. Must type a number (" + str(lower_bound) + " - " + str(upper_bound) + "):\t"))
            except ValueError:
                pass
    return answer

#Validates a yes or no question until, looping until a Y or N is given.
def validate_yn(message: str):
    answer = input("\n" + message + " (Y or N):\t")         #Ex. "\nWould you like to load a save? (Y or N):\t"
    while answer.upper() != "Y" and answer.upper() != "N":
        answer = input("Invalid input. Please input a \"Y\" or \"N\":\t")
    return answer.upper()


"""
load_mall() takes in a file destination and reads in its contents,
which are in the form of a json file. This then returns a mall class
"""
def load_mall(save_dest: str):
    with open(save_dest, "r") as f:
        data = json.load(f)
    user_mall = Mall(data["mall_name"], data["recalls"], int(data["max_plots"]))

    i = 0
    while "plot" + str(i) in data:
        p_dict = data["plot" + str(i)]  # Nice try p_dicty
        name, description, sqr_feet = p_dict["name"], p_dict["description"], p_dict["square_feet"]
        match p_dict["class_type"]:
            case "Plot":
                new_plot = Plot(name, description, sqr_feet)
            case "Store":
                new_plot = Store(name, description, sqr_feet)
            case "Restaurant":
                new_plot = Restaurant(name, description, sqr_feet, p_dict["seats"])
            case _: #Department
                new_plot = Department(name, description, sqr_feet)
        user_mall.add_store(new_plot, i)

        n = 0
        while "item" + str(n) in p_dict:
            i_dict = p_dict["item" + str(n)]
            name, description, price = i_dict["name"], i_dict["description"], i_dict["price"]
            if i_dict["class_type"] == "Item":
                new_product = (Item(name, description, price, i_dict["stock"]))
            else:
                new_product = (Service(name, description, price, i_dict["start_time"], i_dict["end_time"]))
            n += 1

            user_mall.add_product(new_product)      #Add to the mall
            new_plot.add_product(new_product)   #Add to the active store
        i += 1

    return user_mall


"""
save_mall() takes in a file destination and the mall object, saving all of its contents
to a json file in the /saves/ directory, where it can be loaded later
"""
def save_mall(save_dest: str, user_mall: Mall):
    save_data = {"mall_name": user_mall.name, "recalls": user_mall.recalls, "max_plots": user_mall.max_plots}

    i = 0
    for plot in user_mall.plot_list:
        save_data["plot" + str(i)] = plot.__dict__()

        if not plot.__class__ is Plot:
            n = 0
            for product in plot.list:
                save_data["plot" + str(i)]["item" + str(n)] = product.__dict__()
                n += 1
        i += 1

    with open(save_dest, mode="w", encoding="utf-8") as f:
        json.dump(save_data, f, sort_keys=True, indent=4)


"""
create_product() runs through the process of creating a product and
returns either an item or a service
"""
def create_product():
    product_name = input("\nWhat is your new product's name?\t")
    product_description = input("Give a short description of your product (Press ENTER for none):\t")
    product_type = int(input("Is your product an item (1) or a service (2)?\t"))
    while product_type < 1 or product_type > 2:
        product_type = input("\nInvalid option. Is your product an item or a service?\t")
    product_price = float(input("What is your product's price:\t"))

    if product_type == 1:
        return Item(product_name, product_description, product_price)

    else:
        return Service(product_name, product_description, product_price)


"""
copy_product() takes in a product and returns a copy of it,
but with a unique amount of stock or time period
"""
def copy_product(product: Product):
    if isinstance(product, Item):
        new_stock = int(input("How much stock should this item have?\t"))
        while new_stock < 0:
            new_stock = int(input("Stock cannot be negative. Input positive integer:\t"))
        return Item(product.name, product.description, product.price, new_stock)
    elif isinstance(product, Service):
        new_start = input("What is the starting period your service is offered? (Format: XX:XX AM)\t")
        new_end = input("What is the ending period your service is offered? (Format: XX:XX PM)\t")
        return Service(product.name, product.description, product.price, new_start, new_end)
    else:
        return Product(product.name, product.description)

"""
cut_center()
"""
def cut_center(string: str, width: int):
    return string[0:width].center(width)

"""
print_mall()
"""
def print_mall(mall: Mall):
    plots = mall.plot_list
    tier_1_plots = ""
    for i in range(0, 7):
        tier_1_plots += "|" + cut_center(plots[i].name, 17) + "|"

    print( ("#"*133 + "\n")*2 + "\n" +
           "|----##-----------|"*7 + "\n" + "|                 |" * 7 + "\n" +
           tier_1_plots + "\n" + "|                 |" * 7 + "\n" + "|----   ----------|"*7 +
           "\n|" + "Walkway".center(129) + " <--Entrance")

    #FIRST UPGRADE
    if mall.max_plots >= 10:
        wall = "\n|" + " "*50 + "|      |" + " "*25 + "|"
        print("|" + "-"*22 + "      " + "-"*23 + "      " + "-"*12 + "   " + "-"*59 + "|" +
              wall*2 + ("\n|" + " "*59 + cut_center(plots[8].name,24) + "|") + wall*3 +
              "\n|" + cut_center(plots[7].name, 50) + "|      |" + "-"*22 + "##-|" + "Courtyard".center(40) +
              wall*3 + "\n|" + " "*59 + cut_center(plots[8].name,24) + "|" + wall*2)

        #SECOND UPGRADE
        if mall.max_plots >= 15:
            tier_3_plots = "\n|      "
            for i in range(10, 15):
                tier_3_plots += "|" + cut_center(plots[i].name, 17) + "|"
            print("|" + "-"*22 + "      " + "-"*23 + "      " + "-"*12 + "   " + "-"*35 + "|" +
                  "\n|" + "Walkway".center(106) + " <--Entrance" + "\n|      " + "|-------   -------|"*5 + "      |" +
                  ("\n|      " + ("|" + " "*17 + "|")*5 + "      |")*2 + tier_3_plots + "      |" +
                  ("\n|      " + ("|" + " "*17 + "|")*5 + "      |")*2 + "\n|      " + "|-------------##--|" * 5 +
                  "      |" + "\n|" + " "*107 + "|")

            #THIRD UPGRADE (Current Final)
            if mall.max_plots >= 25:
                top_tier_3_plots, last_tier_3_plots = "", " "*26
                #For Plots 16 - 18 and 23 - 25
                for i in range(0, 3):
                    top_tier_3_plots += ("|" + "-"*25 + "|" + " "*55 + "|" + "-"*25 + "|"
                                         "\n#" + cut_center(plots[14+i].name, 25) + "|" + " "*55 +    #Left Store
                                         "|" + cut_center(plots[24 - i].name, 25) + "#" +           #Right Store
                                         ("\n|" + " "*25 + "|" + " "*55 + "|" + " "*25 + "|")*2 + "\n")
                top_tier_3_plots += "|" + "-"*25 + "|" + "-"*50 + "|    |" + "-"*25 + "|\n"

                # For Plots 19 - 22
                for i in range(18, 22):
                    last_tier_3_plots += "|" + cut_center(plots[i].name, 11) + "|"

                print(top_tier_3_plots + (" "*26 +("|" + " "*11 + "|")*4 + "    |\n")*2 + last_tier_3_plots +
                      "    |\n" + (" "*26 +("|" + " "*11 + "|")*4 + "    |\n")*2 + " "*26 +
                      ("|" + "-"*11 + "|")*4 + "####| <-(Emergency Exit)" )

            else:
                print("|" + "-" * 107 + "|")

        else:
            print("|" + "-"*50 + "|------|" +"-"*25 + "|")

    else:
        print("|" + "-" * 131 + "|")

    print("\n" + ("#"*133 + "\n")*2)
    mall.print_keys()


#Mall Tiers for number of plots allowed in the mall
#mall_tier_1 = 10
#mall_tier_2 = 15
#mall_tier_3 = 25 #Current Max Tier
#Second Floors??