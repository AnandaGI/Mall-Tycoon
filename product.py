"""
Creator:    Ananda Irwin
Purpose:    Create product classes for use in stores.
Updated:    10/14/2024
"""

"""
General Product Class - Simply placeholder than can be put on shelves
"""
class Product:
    def __init__(self, name: str, description: str, price: float = 0):
        if price < 0.0:
            raise ValueError

        self.__name = name
        self.__description = description
        self.__price = price

    def __dict__(self):
        return {
            "class_type": self.__class__.__name__,
            "name": self.__name,
            "description": self.__description
        }

    def __eq__(self, other):
        return self.__name == other.name

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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price < 0.0:
            raise ValueError
        self.__price = new_price

    def print_stats(self):
        print(self.__name + " Stats\nDescription: " + self.__description)

"""
Item Class - Product that has stock and can be sold or ordered.
"""
class Item(Product):
    def __init__(self, name: str, description, price: float, stock: int = 0):
        super().__init__(name, description, price)
        self.__stock = stock

    def __dict__(self):
        item_dict = super().__dict__()
        item_dict["price"] = self.price
        item_dict["stock"] = self.__stock
        return item_dict

    @property
    def stock(self):
        return self.__stock

    def restock(self, amount: int):
        self.__stock += amount

    def deplete_stock(self, amount):
        self.__stock -= amount

    def print_stats(self):
        super().print_stats()
        print("Price: " + str(self.price) + "\nStock: " + str(self.__stock))

"""
Service Class - Service that has timeslots and can be booked
"""
class Service(Product):
    def __init__(self, name: str, description: str, price: float, start_time:str = "8:00 AM", end_time:str = "7:00 PM"):
        super().__init__(name, description, price)
        self.__start_time = start_time
        self.__end_time = end_time

    def __dict__(self):
        item_dict = super().__dict__()
        item_dict["price"] = self.price
        item_dict["start_time"] = self.__start_time
        item_dict["end_time"] = self.__end_time
        return item_dict

    @property
    def time_range(self):
        return self.__start_time + " - " + self.__end_time

    @property
    def start(self):
        return self.__start_time

    @start.setter
    def start(self, new_start: str):
        self.__start_time = new_start

    @property
    def end(self):
        return self.__end_time

    @end.setter
    def end(self, new_end: str):
        self.__end_time = new_end


    def print_stats(self):
        super().print_stats()
        print("Price: " + str(self.price))
        print("Starting Availability: " + self.__start_time + "\nEnding Availability: " + self.__end_time)