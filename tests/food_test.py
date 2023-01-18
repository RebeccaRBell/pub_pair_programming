import unittest

from src.food import Food
from src.customer import Customer

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Burger", 9, 2)
        self.customer = Customer("Rupert", 10, 19)

    def test_eat_food(self):
        self.food.eat_food(self.customer, self.food)
        self.assertEqual(-2, self.customer.drunkenness)
