import unittest
from src.customer import Customer
from src.drink import Drink


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Rupert", 10, 17)
        self.drink = Drink("Tennents", 2.50, 2)

    def test_check_drunkenness(self):
        # self.customer.customer_drunkenness(self.customer.drunkenness)
        self.assertEqual(10, self.customer.customer_drunkenness(self.customer.drunkenness))

    # def test_increase_drunkenness(self):
    #     self.customer.increase_drunkenness(self.drink.name)
    #     self.assertEqual(2, self.customer.increase_drunkenness(self.drink.alcohol_level))
