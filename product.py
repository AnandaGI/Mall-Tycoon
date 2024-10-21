"""
Creator:    Ananda Irwin
Purpose:    Create product classes for use in stores.
Updated:    10/14/2024
"""

"""
General Product Class - Simply placeholder than can be put on shelves
"""
class Product:
    def __init__(self, name: str, description = ""):
        self.__name = name
        self.__description = description

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

"""
Item Class - Product that has stock and can be sold or ordered.
"""
class Item(Product):
    def __init__(self, name: str, description, price: float, stock: int = 0):
        super().__init__(name, description)
        self.__stock = stock
        self.__price = price

    def restock(self, amount: int):
        self.__stock += amount

    def deplete_stock(self, amount):
        self.__stock -= amount

    @property
    def stock(self):
        return self.__stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        self.__price = new_price

"""
Service Class - Service that has timeslots and can be booked
"""
class Service(Product):
    def __init__(self, name: str, description, price: float, start_time: str = "8:00 AM", end_time: str = "7:00 PM"):
        super().__init__(name, description)
        self.__price = price
        self.__start_time = start_time
        self.__end_time = end_time

    """
    def add_timeslot(self, time_slot: str):  #Should be in form "XX:XX (AM/PM) - XX:XX (AM/PM)"
        if self.slots == 0:
            self.time_slots.append(time_slot)

        #Use while no sorting algorithm in place yet
        else:
            for i in range (0, len(self.time_slots)):
                print(str(i+1) + ")\t" + self.time_slots[i])

            index = int(input("Where would you like to insert this time?\t"))
            while index < 1 or index > self.slots:
                index = int(input("Invalid index. Where would you like to insert this time?\t"))

            self.time_slots.insert(index-1, time_slot)

        self.slots += 1

    def remove_timeslot(self, index):       #Returns and removes the timeslot so that it can be added elsewhere.
        return self.time_slots.pop(index)
    """

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        self.__price = new_price

    @property
    def time_range(self):
        return self.__start_time + " - " + self.__end_time


"""
Product Functions
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
        return Item(product_name, product_description, item_quantity, product_price)

    else:
        #Include a function here to read in a list of timeslots from a file
        return Service(product_name, product_description, product_price)

def copy_product(product: Product):
    if isinstance(product, Item):
        new_stock = int(input("How much stock should this item have?\t"))
        while new_stock < 0:
            new_stock = int(input("Stock cannot be negative. Input positive integer:\t"))
        return Item(product.name, product.description, product.price, new_stock)
    elif isinstance(product, Service):
        return Service(product.name, product.description, product.price)
    else:
        return Product(product.name, product.description)