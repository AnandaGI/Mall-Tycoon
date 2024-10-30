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
        self.__plot_list = []          #List of stores
        self.__all_products = []        #All products that have been created during the course of the mall's lifespan

    def __dict__(self):
        plot_list = []
        for plot in self.__plot_list:
            plot_list.append(plot.__dict__)
            product_list = []
            if not plot.__class__ is Plot:
                for product in plot.list:
                    product_list.append(product.__dict__)
                plot_list[-1]["product_list"] = product_list
        return {
            "name": self.__name,
            "plot_list": self.__plot_list
        }

    @property
    def name(self):
        return self.__name

    @property
    def num_stores(self):
        return len(self.__plot_list)

    @property
    def num_items(self):
        return len(self.__all_products)

    @property
    def plot_list(self):
        return self.__plot_list

    def add_store(self, plot: Plot):
        self.__plot_list.append(plot)

    def get_store(self, index):
        return self.__plot_list[index]

    def add_product(self, product: Product):
        if not product in self.__all_products:    #Don't add if product exists already
            self.__all_products.append(product)

    #This will go through all the stores and delete all instances of some particular product
    def recall_product(self, product: Product):
        for store in self.__plot_list:
            if not isinstance(store, Plot):  # As long as the store is not a plot
                for store_product in store.list:
                    if store_product == product:
                        store.remove_product(store_product)

    def display_mall(self):
        print("\n" + self.name + " Current Plots\n" + ("-"*20))
        for store in self.__plot_list:
            print(store.name + " | " + store.description)

    def display_all_plots(self):
        print("\n" + self.name + " Current Plots\n" + ("-"*20))
        for store in self.__plot_list:
            store.display_catalog()

    def display_numbered_plots(self):
        print("\n" + self.name + " Current Plot List\n" + ("-" * 20))
        for i in range(0, self.num_stores):
            print((i+1), ")\t", self.__plot_list[i].name)

    def display_products(self):
        print("\nAll Previous Products\n" + ("-" * 20))
        if self.num_stores == 0:
            print("There are no products in your mall yet.")
        else:
            i = 1
            for product in self.__all_products:
                print(i, ")\t", product.name)
                i += 1

    def get_item(self, index: int):
        return self.__all_products[index]