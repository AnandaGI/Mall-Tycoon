"""
Creator:    Ananda Irwin
Purpose:    Create stores, which sell items, services, or both
Updated:    10/14/2024
"""
from product import *

class Plot:
    def __init__(self, name: str, description: str, square_feet: int):
        self.__name = name
        self.__description = description
        self.__square_feet = square_feet

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
    def description(self, new_description: str):
        self.__description = new_description

    @property
    def square_feet(self):
        return self.__square_feet

    @square_feet.setter
    def square_feet(self, square_feet):
        self.__square_feet = square_feet


"""
Restaurant - has a limited capacity and a menu of food items
"""
class Restaurant(Plot):
    def __init__(self, name: str, description: str, sqr_feet: int, seats: int):
        super().__init__(name, description, sqr_feet)
        self.__seats = seats #How many guests can the restaurant seat?
        self.__menu = []

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, num_seats: int):
        self.__seats = num_seats

    @property
    def list(self):
        return self.__menu

    #Could hypothetically create new product type recipe that utilizes other products in its composition, setting
    #the restaurant class apart from its peers somewhat
    def add_product(self, food: Item):
        if isinstance(food, Item):
            self.__menu.append(food)
            return 1
        else:
            return 0

    def display_menu(self):
        #If no products exist to display, notify user
        if len(self.__menu) == 0:
            print("No products to display.")
            return

        i = 1
        #Print all items
        for curr_product in self.__menu:
            if isinstance(curr_product, Item):
                print(str(i) + ")\t" + curr_product.name + " | " + curr_product.stock)
                i += 1

        print("-" * 20)
        #End


"""
Department - an function of the mall for guests to interact with, such as security or customer service
"""
class Department(Plot):
    def __init__(self, name: str, description: str, sqr_feet: int):
        super().__init__(name, description, sqr_feet)
        souvenir = Product(self.name + " Department Souvenir", "A souvenir from the " + self.name + " Department.")
        self.__functions = [souvenir]

    @property
    def list(self):
        return self.__functions

    def add_product(self, service: Service):
        if isinstance(service, Service):
            self.__functions.append(service)
            return 1
        else:
            return 0

    def display_department(self):
        print("\nHi, welcome to " + self.name + "!\nWe can provide you with the following services:")
        i = 1
        for curr_product in self.__functions:
            if isinstance(curr_product, Service):
                print(str(i) + ")\t" + curr_product.name)
                i += 1

"""
Combo Store - sells both services and items
"""
class Store(Plot):
    def __init__(self, name: str, description: str, sqr_feet: int):
        super().__init__(name, description, sqr_feet)
        self.__product_catalog = []

    @property
    def list(self):
        return self.__product_catalog

    def add_product(self, product: Product):
        self.__product_catalog.append(product)
        return 1

    def display_catalog(self):
        print("\n" + self.name + "'s Product Page\n" + ("-" * 20))

        #If no products exist to display, notify user
        if len(self.__product_catalog) == 0:
            print("No products to display.")
            return

        i = 1
        #Print all items
        print("Products:")
        for curr_product in self.__product_catalog:
            if isinstance(curr_product, Item):
                print(str(i) + ")\t" + curr_product.name + " | " + curr_product.stock)
                i += 1

        print("Services:")
        for curr_product in self.__product_catalog:
            if isinstance(curr_product, Service):
                print(str(i) + ")\t" + curr_product.name)
                i += 1

        print("-" * 20)
        #End