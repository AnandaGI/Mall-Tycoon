"""
Creator:    Ananda Irwin
Purpose:    Create stores, which sell items, services, or both
Updated:    10/14/2024
"""
from xml.sax.handler import property_dom_node

from store import Plot
from product import Product

class Mall:
    def __init__(self, name):
        self.__name = name
        self.__store_list = []          #List of stores
        self.__all_products = []        #All products that have been created during the course of the mall's lifespan
        self.__active_products = []     #The current products that are being created or used

    @property
    def name(self):
        return self.__name

    def add_store(self, plot: Plot):
        self.__store_list.append(plot)

    @property
    def num_stores(self):
        return len(self.__store_list)

    @property
    def num_items(self):
        return len(self.__all_products)

    def get_store(self, index):
        return self.__store_list[index]

    def display_mall(self):
        print("\n" + self.name + " Current Store List\n" + ("-"*20))
        for store in self.__store_list:
            print(store.name + " | " + store.description)

    def display_store_list(self):
        print("\n" + self.name + " Current Store List\n" + ("-" * 20))
        for i in range(0, self.num_stores):
            print((i+1), ")\t", self.__store_list[i])

    #This will go through all the stores and delete all instances of some particular product
    def recall_product(self, product: Product):
        for store in self.__store_list:
            if not isinstance(store, Plot): #As long as the store is not a plot
                for other in store.list:
                    if other == product:
                        store.remove_product(other)

    def add_product(self, product: Product):
        self.__active_products.append(product)
        #If the product already exists in the list of all products
        for prod in self.__all_products:
            if product == prod:
                return          #Return and do not add to all_products if it already exists
        self.__all_products.append(product)

    def clear_products(self):
        self.__active_products.clear()

    def display_products(self):
        print("\nAll Previous Products\n" + ("-" * 20))
        i = 1
        for product in self.__all_products:
            print(i, ")\t", product.name)

    def display_active(self):
        print("\nCurrent Active Products:")
        for product in self.__active_products:
            print(i, ")\t", product.name)

    def get_item(self, index: int):
        return self.__all_products[index]