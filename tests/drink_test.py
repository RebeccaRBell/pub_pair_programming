import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Tennents", 2.50, 2)

    def test_find_drink_by_name(self):
        self.drink.find_drink_by_name(self.drink.name)
        self.assertEqual("Tennents", self.drink.find_drink_by_name(self.drink.name))

    def test_find_alcohol_level(self):
        self.drink.find_alcohol_level(self.drink.name)
        self.assertEqual(2, self.drink.find_alcohol_level(self.drink.alcohol_level))

        