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

    def __str__(self):
        return self.name

    def add_store(self, store: Store):
        self.store_list.append(store)

    def display_mall(self):
        print("\n" + self.name + " Current Store List\n" + ("-"*20))
        for store in self.store_list:
            print(store, "|", store.get_description())
