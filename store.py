"""
Creator:    Ananda Irwin
Purpose:    Create stores, which sell items, services, or both
Updated:    10/14/2024
"""
from product import *

class Store:
    def __init__(self, name: str, description: str, square_feet: int):
        self.name = name
        self.description = description
        self.square_feet = square_feet

    def __str__(self):
        return self.name

    def get_description(self):
        return self.description

    def set_name(self, new_name: str):
        self.name = new_name

    def set_description(self, new_description: str):
        self.description = new_description

class RetailStore(Store):
    def __init__(self, name: str, description: str, sqr_feet: int):
        super().__init__(name, description, sqr_feet)
        self.catalog = []

    def __str__(self):
        return self.name

    def add_product(self, item: Item):
        if isinstance(item, Item):
            self.catalog.append(item)
        else:
            print("Cannot add a service to an retail store.")

    def display_catalog(self):
        print("\n" + self.name + "'s Product Page\n" + ("-" * 20))
        i = 1
        for item in self.catalog:
            print("("+str(i)+")", item, "|", item.stock, item.get_description())
            i+=1

        print("-" * 20)

class ServiceStore(Store):
    def __init__(self, name: str, description: str, sqr_feet: int):
        super().__init__(name, description, sqr_feet)
        self.catalog = []

    def add_product(self, service: Service):
        if isinstance(service, Service):
            self.catalog.append(service)
        else:
            print("Cannot add an item to a service-based store.")

    def display_catalog(self):
        print("\n" + self.name + "'s Services\n" + ("-" * 20))
        i = 1
        for service in self.catalog:
            print("("+str(i)+") " + str(service))
            i+=1

        print("-" * 20)

class ComboStore(Store):
    def __init__(self, name: str, description: str, sqr_feet: int):
        super().__init__(name, description, sqr_feet)
        self.item_catalog = []
        self.service_catalog = []

    def add_item(self, item: Item):
        self.item_catalog.append(item)

    def add_service(self, service: Service):
        self.service_catalog.append(service)

    def add_product(self, product: Product):
        if isinstance(product, Item):
            self.add_item(product)
        elif isinstance(product, Service):
            self.add_service(product)
        else:
            print("\nInvalid product to add to store.")

    def display_catalog(self):
        print("\n" + self.name + "'s Product Page\n" + ("-" * 20))

        #If there are items in the store's catalog
        if len(self.item_catalog) > 0:
            i = 1
            for item in self.catalog:
                print("(" + str(i) + ")", item, "|", item.stock, item.get_description())
                i += 1

        #If there are services in the store's catalog
        if len(self.service_catalog) > 0:
            for service in self.catalog:
                print("(" + str(i) + ") " + str(service))
                i += 1

        if len(self.item_catalog) > 0 and len(self.service_catalog) > 0:
            print("No products to display.")