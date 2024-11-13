"""
Creator:    Ananda Irwin
Purpose:    Create stores, which sell items, services, or both
Updated:    10/14/2024
"""
from store import Plot
from product import Product
import json

#ADD SLOTS TO THE MALL SO THAT YOU CAN START HAVE A STARTER MALL
class Mall:
    def __init__(self, name: str, recalls: int = 0, max_plots: int = 7):
        self.__name = name
        self.__plot_list = [Plot("None", "", 0) for i in range(0,25)]          #List of stores
        self.__all_products = []        #All products that have been created during the course of the mall's lifespan
        self.__recalls = recalls
        self.__max_plots = max_plots    #Maximum number of plots in a mall, can be upgraded.

    """
    Properties
    """
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

    @property
    def recalls(self):
        return self.__recalls

    @property
    def max_plots(self):
        return self.__max_plots

    """
    Functions
    """
    def add_store(self, plot: Plot, index):
        self.__plot_list[index] = plot

    def get_store(self, index):
        return self.__plot_list[index]

    def get_item(self, index: int):
        return self.__all_products[index]

    def add_product(self, product: Product):
        if not product in self.__all_products:    #Don't add if product exists already
            self.__all_products.append(product)

    #This will go through all the stores and delete all instances of some particular product
    def recall_product(self, product: Product):
        for store in self.__plot_list:
            if not store.__class__.__name__ == "Plot":  # As long as the store is not a plot
                for store_product in store.list:
                    if store_product == product:
                        store.remove_product(store_product)
                        self.__recalls += 1
        self.__all_products.remove(product) #Also removes the product from the mall itself

    def remove_plot(self, index):
        self.__plot_list[index] = Plot("None", "", 0)

    def display_mall(self):
        print("\n" + self.name + " Current Plots\n" + ("-"*20))
        for store in self.__plot_list:
            print(store.name + " | " + store.description)

    def display_all_plots(self):
        print("\n" + self.name + " Current Plots\n" + ("-"*20))
        for plot in self.__plot_list:
            plot.display_catalog()

    def display_products(self):
        print("\nAll Previous Products\n" + ("-" * 20))
        if self.num_items == 0:
            print("There are no products in your mall yet.")
        else:
            i = 1
            for product in self.__all_products:
                print(i, ")\t", product.name)
                i += 1

    def print_keys(self):
        print("Store Key:")
        for i in range(0, self.__max_plots):
            print( (str(i + 1) + ".\t" + self.plot_list[i].name).ljust(30), end=""  )
            if i % 2 == 0:
                print()

    def upgrade(self):
        match self.__max_plots:
            case 7:
                self.__max_plots = 10
                #for i in range(7, 10):
                #    self.add_store(Plot("None", "", 0), i)
            case 10:
                self.__max_plots = 15
            case 15:
                self.__max_plots = 25
            case 25:
                print("Currently at max tier.")

    def downgrade(self):
        match self.__max_plots:
            case 7:
                print("Currently at lowest tier.")
            case 10:
                self.__max_plots = 7
                for i in range(7, 10):
                    self.remove_plot(i)
            case 15:
                self.__max_plots = 10
                for i in range(10, 15):
                    self.remove_plot(i)
            case 25:
                self.__max_plots = 15
                for i in range(15, 25):
                    self.remove_plot(i)