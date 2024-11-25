
import sys
import unittest
from unittest.mock import patch
sys.path.append("../MallTycoon")
from store import *
from product import Product

class TestPlot(unittest.TestCase):
    def setUp(self):
        self.plot = Plot("Sample Plot", "Sample Description")
    
    def tearDown(self):
        pass

    # Test Getters
    def test_name(self):
        self.assertEqual("Sample Plot", self.plot.name)

    def test_description(self):
        self.assertEqual("Sample Description", self.plot.description)

    def test_sqr_feet(self):
        self.assertEqual(2000, self.plot.square_feet)

    def test_dict(self):
        self.assertEqual({"class_type": "Plot", "name": "Sample Plot", "description": "Sample Description",
                          "square_feet": 2000}, self.plot.__dict__())

    #Test Setters
    def test_set_name(self):
        self.plot.name = "New Name"
        self.assertEqual("New Name", self.plot.name)
        self.assertEqual({"class_type": "Plot", "name": "New Name", "description": "Sample Description",
                          "square_feet": 2000}, self.plot.__dict__())

    def test_set_description(self):
        self.plot.description = "New Description"
        self.assertEqual("New Description", self.plot.description)
        self.assertEqual({"class_type": "Plot", "name": "Sample Plot", "description": "New Description",
                          "square_feet": 2000}, self.plot.__dict__())

    def test_set_sqr_feet(self):
        self.plot.square_feet = 2500
        self.assertEqual(2500, self.plot.square_feet)
        self.assertEqual({"class_type": "Plot", "name": "Sample Plot", "description": "Sample Description",
                          "square_feet": 2500}, self.plot.__dict__())

    @patch("builtins.print")
    def test_stats(self, mocked_print):
        self.plot.display_catalog()
        mocked_print.assert_called_with("\nSample Plot Description Page\n\"Sample Description\"\n" + "-"*20)

class TestRetailer(unittest.TestCase):
    def setUp(self):
        self.retailer = Retailer("Sample Retailer", "Sample Description")
        self.retailer.add_product(Product("SP", "SD"))

    def tearDown(self):
        pass

    def test_list(self):    #This does not check if the description is the same because it only compares names.
        self.assertEqual([Product("SP", "SD")], self.retailer.list)

    def test_num_prod(self):
        self.assertEqual(1, self.retailer.num_products)

    def test_get_prod(self):
        self.assertEqual("SP", self.retailer.get_product(0).name)
        self.assertEqual("SD", self.retailer.get_product(0).description)

    def test_add_product(self):
        self.retailer.add_product(Product("New Product", "W/ New Description"))
        self.assertEqual("New Product", self.retailer.get_product(1).name)
        self.assertEqual("W/ New Description", self.retailer.get_product(1).description)

    def test_remove_product(self):
        self.retailer.remove_product(Product("SP", "SD"))
        self.assertEqual([], self.retailer.list)

    @patch("builtins.print")
    def test_stats(self, mocked_print):
        self.retailer.add_product(Item("NI", "SD", 9.99, 50))
        self.retailer.list_type(Item)
        mocked_print.assert_called_with("2)\tNI | 50 | $9.99")

    @patch("builtins.print")
    def test_display_catalog(self, mocked_print):
        self.retailer.display_catalog()
        mocked_print.assert_called_with("\nSample Retailer Overview Page\n\"Sample Description\"\n" + "-"*20)

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.restaurant = Restaurant("Sample Restaurant", "Sample Description", 2000, 50)
        self.restaurant.add_product(Item("Food", "SD", 9.99, 50))

    def tearDown(self):
        pass

    def test_seats(self):
        self.assertEqual(50, self.restaurant.seats)

    def test_dict(self):
        self.assertEqual({"class_type": "Restaurant", "name": "Sample Restaurant",
                          "description": "Sample Description", "square_feet": 2000, "seats": 50},
                         self.restaurant.__dict__())

    #Display catalog only uses above functions that we know work (Also it doesn't really test well)

    def test_add_prod(self):
        self.restaurant.add_product(Item("New Food", "SD", 4.99, 50))
        self.assertEqual(True, Item("New Food", "SD", 4.99, 50) in self.restaurant.list)
        self.assertEqual("SD", self.restaurant.get_product(1).description)
        self.assertEqual(4.99, self.restaurant.get_product(1).price)
        self.assertEqual(50, self.restaurant.get_product(1).stock)

    def test_add_prod_invalid(self):
        self.restaurant.add_product(Service("New Service", "SD", 4.99))
        self.assertEqual(False, Service("New Service", "SD", 4.99) in self.restaurant.list)

    def test_set_seats(self):
        self.restaurant.seats = 95
        self.assertEqual(95, self.restaurant.seats)

class TestDepartment(unittest.TestCase):
    def setUp(self):
        self.dep = Department("Sample Department", "Sample Description", 2000)
        self.dep.add_product(Service("Service", "SD", 9.99))

    def tearDown(self):
        pass

    def test_add_prod(self):
        self.dep.add_product(Service("New Service", "SD", 4.99))
        self.assertEqual(True, Item("New Service", "SD", 4.99,) in self.dep.list)
        self.assertEqual("SD", self.dep.get_product(1).description)
        self.assertEqual(4.99, self.dep.get_product(1).price)
        self.assertEqual("8:00 AM - 7:00 PM", self.dep.get_product(1).time_range)

    def test_add_prod_invalid(self):
        self.dep.add_product(Item("New Item", "SD", 4.99))
        self.assertEqual(False, Item("New Item", "SD", 4.99) in self.dep.list)

    #Display Catalog not tested for similar reasons as above

#Store does not need to be tested, only difference is display_catalog which, like the above,
#cannot be easily tested and is composed of functions proven to work.

