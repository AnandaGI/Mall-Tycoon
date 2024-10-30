import json, os
from mall import Mall
from store import *
from product import *

#Validates that an integer is within a given range, looping until a valid integer can be returned
def validate_bounds(message: str, lower_bound: int, upper_bound: int, zero_exit=False):
    if zero_exit:
        message = "\n" + message + " (" + str(lower_bound+1) + " - " + str(upper_bound) + ")" + " (0 to exit)"
    else:
        message = "\n" + message + " (" + str(lower_bound) + " - " + str(upper_bound) + ")"

    answer = int(input(message + ":\t"))
    while answer < lower_bound or answer > upper_bound:
        answer = int(input("Invalid choice. Must type a number " + str(lower_bound) + " - " + str(upper_bound) + ":\t"))
    return answer

#Validates a yes or no question until, looping until a Y or N is given.
def validate_yn(message: str):
    answer = input("\n" + message + " (Y or N):\t")         #Ex. "\nWould you like to load a save? (Y or N):\t"
    while answer.upper() != "Y" and answer.upper() != "N":
        answer = input("Invalid input. Please input a \"Y\" or \"N\":\t")
    return answer


"""
load_mall() takes in a file destination and reads in its contents,
which are in the form of a json file. This then returns a mall class
"""
def load_mall(save_dest: str):
    with open(save_dest, "r") as f:
        data = json.load(f)
    user_mall = Mall(data["mall_name"])

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
        user_mall.add_store(new_plot)

        n = 0
        while "item" + str(n) in p_dict:
            i_dict = p_dict["item" + str(n)]
            name, description, price = i_dict["name"], i_dict["description"], i_dict["price"]
            if i_dict["class_type"] == "Item":
                user_mall.add_product(Item(name, description, price, i_dict["stock"]))
            else:
                user_mall.add_product(Service(name, description, price, i_dict["start_time"], i_dict["end_time"]))
            n += 1

        for product in user_mall.active_products:
            new_plot.add_product(product)
        user_mall.clear_products()
        i += 1

    return user_mall


"""
save_mall() takes in a file destination and the mall object, saving all of its contents
to a json file in the /saves/ directory, where it can be loaded later
"""
def save_mall(save_dest: str, user_mall: Mall):
    save_data = {"mall_name": user_mall.name}

    i = 0
    for plot in user_mall.store_list:
        save_data["plot" + str(i)] = plot.__dict__()

        if not plot.__class__ is Plot:
            n = 0
            for product in plot.list:
                save_data["plot" + str(i)]["item" + str(n)] = product.__dict__()
                n += 1
        i += 1

    with open(save_dest, mode="a", encoding="utf-8") as f:
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
        item_quantity = int(input("How much stock does this item have? Must be positive integer:\t"))
        return Item(product_name, product_description, product_price, item_quantity)

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