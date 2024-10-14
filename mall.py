"""
Creator:    Ananda Irwin
Purpose:    Create stores, which sell items, services, or both
Updated:    10/14/2024
"""

class Mall:
    def __init__(self, name):
        self.name = name
        self.mall_list = []

    def __str__(self):
        return self.name