import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Duck and Frog", 500, "Tennents")
        self.drink = Drink("Tennents", 2.50, 2)
        self.customer = Customer("Rupert", 10, 19)

    def test_of_drinking_age(self):
        self.pub.of_drinking_age(self.customer.age)
        self.assertEqual(True, self.pub.of_drinking_age(self.customer.age))

    def test_sell_a_drink(self):
        self.pub.sell_a_drink(2.50, self.customer.age)
        self.assertEqual(502.50, self.pub.till)
        
    def test_buy_a_drink(self):
        self.customer.buy_a_drink(2.50)
        self.assertEqual(7.50, self.customer.wallet)

    