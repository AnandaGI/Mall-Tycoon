"""
Creator:    Ananda Irwin
Purpose:    Create stores, which sell items, services, or both
Updated:    10/14/2024
"""

from store import Store

class Mall:
    def __init__(self, name):
        self.name = name
        self.store_list = []
        self.num_stores = 0

    def __str__(self):
        return self.name

    def add_store(self, store: Store):
        self.store_list.append(store)
        self.num_stores += 1

    def get_num_stores(self):
        return self.num_stores

    def get_store(self, index):
        return self.store_list[index]

    def display_mall(self):
        print("\n" + self.name + " Current Store List\n" + ("-"*20))
        for store in self.store_list:
            print(store, "|", store.get_description())

    def display_store_list(self):
        print("\n" + self.name + " Current Store List\n" + ("-" * 20))
        for i in range(0, len(self.store_list)):
            print((i+1), ")\t", self.store_list[i])
