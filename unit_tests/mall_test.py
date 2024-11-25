import sys
import unittest
from unittest.mock import patch
sys.path.append("../MallTycoon")
from mall import Mall
from store import Plot, Store
from product import Item

class TestMall(unittest.TestCase):
    def setUp(self):
        self.mall = Mall("User Mall", 0, 7)

    def tearDown(self):
        pass

    #Test Getters
    def test_name(self):
        self.assertEqual("User Mall", self.mall.name)

    def test_num_items(self):
        self.assertEqual(0, self.mall.num_items)

    def test_plot_list(self):
        for plot in self.mall.plot_list:            #Check every plot is equal initially
            self.assertEqual("_", plot.name)
            self.assertEqual("", plot.description)
            self.assertEqual(0, plot.square_feet)
        self.assertEqual(25, len(self.mall.plot_list))

    def test_recalls(self):
        self.assertEqual(0, self.mall.recalls)

    def test_max_plots(self):
        self.assertEqual(7, self.mall.max_plots)

    def get_store(self):
        self.assertEqual("_", self.mall.get_store(0).name)
        self.assertEqual("", self.mall.get_store(0).description)
        self.assertEqual(0, self.mall.get_store(0).square_feet)

    #Test Functions
    def test_add_store(self):
        self.mall.add_store(Plot("New Plot", "", 2000), 0)
        self.assertEqual("New Plot", self.mall.get_store(0).name)
        self.assertEqual("", self.mall.get_store(0).description)
        self.assertEqual(2000, self.mall.get_store(0).square_feet)

    def test_add_prod(self):
        self.mall.add_product(Item("Sample Item", "SD", 9.99, 50))
        self.assertEqual("Sample Item", self.mall.get_item(0).name)
        self.assertEqual("SD", self.mall.get_item(0).description)
        self.assertEqual(9.99, self.mall.get_item(0).price)
        self.assertEqual(50, self.mall.get_item(0).stock)

    def test_get_item(self):
        self.mall.add_product(Item("Sample Item", "SD", 9.99, 50))
        item = self.mall.get_item(0)
        self.assertEqual(Item("Sample Item", "SD", 9.99, 50), item)

    def test_recall(self):
        self.mall.add_store(Store("P1", "", 2000), 0)
        self.mall.add_store(Store("P2", "", 2000), 1)
        self.mall.add_product(Item("Sample Item", "", 9.99, 50))
        for i in range(0, 2):
            self.mall.get_store(i).add_product( self.mall.get_item(0) )
            self.assertEqual("Sample Item", self.mall.get_store(i).get_product(0).name) #Confirm the item is added
            self.assertEqual(1, len(self.mall.get_store(i).list))

        self.mall.recall_product(Item("Sample Item", "", 9.99, 50))

        for i in range(0, 2):
            self.assertEqual(0, len(self.mall.get_store(i).list))   #Confirm item was removed
        self.assertEqual(2, self.mall.recalls)

    def test_remove_plot(self):
        self.mall.add_store(Store("P1", "", 2000), 0)
        self.assertEqual("P1", self.mall.get_store(0).name) #Confirm store added

        self.mall.remove_plot(0)
        self.assertEqual("_", self.mall.get_store(0).name)  #Confirm store removed
        self.assertEqual("Plot", self.mall.get_store(0).__class__.__name__)

    @patch("builtins.print")
    def test_upgrade(self, mocked_print):
        self.assertEqual(7, self.mall.max_plots)
        self.mall.upgrade()
        self.assertEqual(10, self.mall.max_plots)
        self.mall.upgrade()
        self.assertEqual(15, self.mall.max_plots)
        self.mall.upgrade()
        self.assertEqual(25, self.mall.max_plots)
        self.mall.upgrade()
        mocked_print.assert_called_with("Currently at max tier.")

    @patch("builtins.print")
    def test_downgrade(self, mocked_print):
        self.mall = Mall("User_Mall", 0, 25)
        self.assertEqual(25, self.mall.max_plots)
        self.mall.downgrade()
        self.assertEqual(15, self.mall.max_plots)
        self.mall.downgrade()
        self.assertEqual(10, self.mall.max_plots)
        self.mall.downgrade()
        self.assertEqual(7, self.mall.max_plots)
        self.mall.downgrade()
        mocked_print.assert_called_with("Currently at lowest tier.")

    #Testing print functions is not exactly feasible here.