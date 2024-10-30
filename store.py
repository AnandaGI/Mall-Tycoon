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

    def __dict__(self):
        return {
            "class_type": self.__class__.__name__,
            "name": self.__name,
            "description": self.__description,
            "square_feet": self.__square_feet
        }

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

    @property
    def num_products(self):
        return len(self.__product_list)

    def add_product(self, product: Product):
        self.__product_list.append(product)
        return 1

    def remove_product(self, product: Product):
        self.__product_list.remove(product)

    def get_product(self, index: int):
        return self.__product_list[index]

    #Prints all the objects of some class type
    def list_type(self, product_type):
        i = 1
        for curr_product in self.__product_list:
            if isinstance(curr_product, product_type):
                if product_type == Item:
                    print(str(i) + ")\t" + curr_product.name + " | " + str(curr_product.stock) + " | $" + str(curr_product.price))
                elif product_type == Service:
                    print(str(i) + ")\t" + curr_product.name + " | " + curr_product.time_range + " | $" + str(curr_product.price))
                else:
                    print(str(i) + ")\t" + curr_product.name)
            i += 1

    def display_catalog(self):
        print("\n" + self.name + "'s Overview Page\n\"" + self.description + "\"\n" + ("-" * 20))

        # If no products exist to display, notify user
        if len(self.__product_list) == 0:
            print("No products to display.")
            return False
        return True
        

"""
Restaurant - has a limited capacity and a menu of food items
"""
class Restaurant(Retailer):
    def __init__(self, name: str, description: str, sqr_feet: int, seats: int = 95):
        super().__init__(name, description, sqr_feet)
        self.__seats = seats #How many guests can the restaurant seat?

    def __dict__(self):
        self_dict = super().__dict__()
        self_dict["seats"] = self.__seats
        return self_dict

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
        if super().display_catalog():
            print("Available Dishes:")
            self.list_type(Item)
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
        self.list_type(Service)


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
        self.list_type(Item)

        print("Services:")
        self.list_type(Service)

        print("-" * 20)
        #End