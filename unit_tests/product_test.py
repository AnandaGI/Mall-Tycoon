
import sys
import unittest
from unittest.mock import patch
sys.path.append("../MallTycoon")
from product import *

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Sample Product", "Sample Description", 9.99)

    def tearDown(self):
        pass

    #Test Getters
    def test_name(self):
        self.assertEqual("Sample Product", self.product.name)

    def test_description(self):
        self.assertEqual("Sample Description", self.product.description)

    def test_dict(self):
        self.assertEqual({"class_type": "Product", "name": "Sample Product", "description": "Sample Description",
                          "price": 9.99}, self.product.__dict__())

    @patch("builtins.print")
    def test_stats(self, mocked_print):
        self.product.print_stats()
        mocked_print.assert_called_with("Sample Product Stats\nDescription: Sample Description")

    #Test Setters
    def test_set_name(self):
        self.product.name = "New Name"
        self.assertEqual("New Name", self.product.name)
        self.assertEqual({"class_type": "Product", "name": "New Name", "description": "Sample Description",
                          "price": 9.99}, self.product.__dict__())

    def test_set_description(self):
        self.product.description = "New Description"
        self.assertEqual("New Description", self.product.description)
        self.assertEqual({"class_type": "Product", "name": "Sample Product", "description": "New Description",
                          "price": 9.99}, self.product.__dict__())

    def test_equal_override(self):
        self.assertEqual(True, self.product == Product("Sample Product", "", 0))


class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item("Sample Item", "Sample Description", 9.99, 10)

    def tearDown(self):
        pass

    #Test New Stock Attribute
    def test_stock(self):
        self.assertEqual(10, self.item.stock)

    def test_restock(self):
        self.item.restock(5)
        self.assertEqual(15, self.item.stock)
        self.assertEqual({"class_type": "Item", "name": "Sample Item", "description": "Sample Description",
                          "price": 9.99, "stock": 15}, self.item.__dict__())

    def test_deplete_stock(self):
        self.item.deplete_stock(5)
        self.assertEqual(5, self.item.stock)
        self.assertEqual({"class_type": "Item", "name": "Sample Item", "description": "Sample Description",
                          "price": 9.99, "stock": 5}, self.item.__dict__())

    def test_dict(self):
        self.assertEqual({"class_type": "Item", "name": "Sample Item", "description": "Sample Description",
                          "price": 9.99, "stock": 10}, self.item.__dict__())

    @patch("builtins.print")
    def test_stats(self, mocked_print):
        self.item.print_stats()
        mocked_print.assert_called_with("Price: 9.99\nStock: 10")

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service("Sample Service", "Sample Description", 9.99)

    def tearDown(self):
        pass

    #Getters
    def test_start(self):
        self.assertEqual("8:00 AM", self.service.start)

    def test_end(self):
        self.assertEqual("7:00 PM", self.service.end)

    def test_range(self):
        self.assertEqual("8:00 AM - 7:00 PM", self.service.time_range)

    #Setters
    def test_set_start(self):
        self.service.start = "6:00 AM"
        self.assertEqual("6:00 AM", self.service.start)
        self.assertEqual({"class_type": "Service", "name": "Sample Service", "description": "Sample Description",
                          "price": 9.99, "start_time": "6:00 AM", "end_time": "7:00 PM"}, self.service.__dict__())

    def test_set_end(self):
        self.service.end = "9:00 PM"
        self.assertEqual("9:00 PM", self.service.end)
        self.assertEqual({"class_type": "Service", "name": "Sample Service", "description": "Sample Description",
                          "price": 9.99, "start_time": "8:00 AM", "end_time": "9:00 PM"}, self.service.__dict__())

    @patch("builtins.print")
    def test_stats(self, mocked_print):
        self.service.print_stats()
        mocked_print.assert_called_with("Starting Availability: 8:00 AM\nEnding Availability: 7:00 PM")

    def test_dict(self):
        self.assertEqual({"class_type": "Service", "name": "Sample Service", "description": "Sample Description",
                          "price": 9.99, "start_time": "8:00 AM", "end_time": "7:00 PM"}, self.service.__dict__())


