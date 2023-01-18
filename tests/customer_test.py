import unittest
from src.customer import Customer
from src.drink import Drink


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Rupert", 10, 17)
        self.drink = Drink("Tennents", 2.50, 2)

    def test_buy_a_drink(self):
        self.customer.buy_a_drink(2.50)
        self.assertEqual(7.50, self.customer.wallet)

    def test_increase_drunkenness(self):
        self.customer.increase_drunkenness(self.drink.alcohol_level)
        self.assertEqual(2, self.customer.drunkenness)


