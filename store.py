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
Generic Store Class, subclass of a simple plot
"""
class Retailer(Plot):
    def __init__(self, name: str, description: str, square_feet: int):
        super().__init__(name, description, square_feet)
        self.__product_list = []

    @property
    def list(self):
        return self.__product_list

    def add_product(self, product: Product):
        self.__product_list.append(product)
        return 1

    def remove_product(self, product_name: str):
        for product in self.__product_list:
            if product_name == product.name:
                self.__product_list.remove(product)
                return 1
        else:
            print("\nProduct not found in catalog.")
            return 0

    #Prints all the objects of some class type
    def list_type(self, start_index: int, product_type):
        i = start_index
        for curr_product in self.__product_list:
            if isinstance(curr_product, product_type):
                if product_type == Item:
                    print(str(i) + ")\t" + curr_product.name + " | " + curr_product.stock)
                elif product_type == Service:
                    print(str(i) + ")\t" + curr_product.name + " | " + curr_product.time_range)
                else:
                    print(str(i) + ")\t" + curr_product.name)
            i += 1

    def display_catalog(self):
        print("\n" + self.name + "'s Overview Page\n" + ("-" * 20))

        # If no products exist to display, notify user
        if len(self.__product_list) == 0:
            print("No products to display.")
            return
        

"""
Restaurant - has a limited capacity and a menu of food items
"""
class Restaurant(Retailer):
    def __init__(self, name: str, description: str, sqr_feet: int, seats: int):
        super().__init__(name, description, sqr_feet)
        self.__seats = seats #How many guests can the restaurant seat?

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, num_seats: int):
        self.__seats = num_seats

    #Could hypothetically create new product type recipe that utilizes other products in its composition, setting
    #the restaurant class apart from its peers somewhat
    def add_product(self, food: Item):
        if isinstance(food, Item):
            super().add_product(food)
        else:
            return 0

    def display_catalog(self):
        super().display_catalog()
        print("Available Dishes:")
        self.list_type(1, Item)
        print("-" * 20)
        #End


"""
Department - an function of the mall for guests to interact with, such as security or customer service
"""
class Department(Retailer):
    def __init__(self, name: str, description: str, sqr_feet: int):
        super().__init__(name, description, sqr_feet)

    def add_product(self, service: Service):
        if isinstance(service, Service):
            super().add_product(service)
        else:
            return 0

    def display_catalog(self):
        super().display_catalog()
        print("\nHi, welcome to " + self.name + "!\nWe can provide you with the following services:")
        self.list_type(1, Service)


"""
Combo Store - sells both services and items
"""
class Store(Retailer):
    def __init__(self, name: str, description: str, sqr_feet: int):
        super().__init__(name, description, sqr_feet)

    def display_catalog(self):
        super().display_catalog()

        i = 1
        #Print all items
        print("Products:")
        self.list_type(i, Item)

        print("Services:")
        self.list_type(i, Service)

        print("-" * 20)
        #End