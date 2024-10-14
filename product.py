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
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

"""
Item Class - Product that has stock and can be sold or ordered.
"""
class Item(Product):
    def __init__(self, name: str, description, stock: int, price: float):
        super().__init__(name, description)
        self.stock = stock
        self.price = price

    def restock(self, amount: int):
        self.stock += amount

    def deplete_stock(self, amount):
        self.stock -= amount

    def change_price(self, new_price):
        self.price = new_price

"""
Service Class - Service that has timeslots and can be booked
"""
class Service(Product):
    def __init__(self, name: str, description, price: float):
        super().__init__(name, description)
        self.price = price
        self.time_slots = []
        self.slots = 0

    def change_price(self, price):
        self.price = price

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