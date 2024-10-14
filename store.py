"""
Creator:    Ananda Irwin
Purpose:    Create stores, which sell items, services, or both
Updated:    10/13/2024
"""
from product import *

class Store:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

class RetailStore(Store):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.catalog = []

    def __str__(self):
        return self.name

    def add_item(self, item: Item):
        self.catalog.append(item)

    def display_catalog(self):
        print("\n" + self.name + "'s Product Page\n" + ("-" * 20))
        i = 1
        for item in self.catalog:
            print("("+str(i)+")", item, "|", item.stock, item.get_description())
            i+=1

        print("-" * 20)

class ServiceStore(Store):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.catalog = []

    def add_service(self, service: Service):
        self.catalog.append(service) #Store services as a tuple with a service and an associated price

    def display_catalog(self):
        print("\n" + self.name + "'s Services\n" + ("-" * 20))
        i = 1
        for service in self.catalog:
            print("("+str(i)+") " + str(service))
            i+=1

        print("-" * 20)

class ComboStore(Store):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.item_catalog = []
        self.service_catalog = []

    def add_item(self, item: Item):
        self.item_catalog.append(item)

    def add_service(self, service: Service):
        self.service_catalog.append(service)

    def display_items(self):
        print("\nProducts:")
        if len(self.item_catalog) > 0:
            for i in range(0, len(self.item_catalog)):
                item = self.item_catalog[i]
                print(str(i + 1) + ")\t", item, "|", item.stock, item.get_description())
            print("-" * 20)

    def display_services(self):
        if len(self.service_catalog) > 0:
            for i in range(0, len(self.service_catalog)):
                service = self.service_catalog[i]
                print(str(i + 1) + ")\t", service, "|", service.get_description())
            print("-" * 20)

    def display_catalog(self):
        print("\n" + self.name + "'s Product Page\n" + ("-" * 20))

        #If there are items in the store's catalog
        if len(self.item_catalog) > 0:
            self.display_items()

        #If there are services in the store's catalog
        if len(self.service_catalog) > 0:
            self.display_services()