class Drink:
    def __init__(self, name, price, alcohol_level):
        self.name = name
        self.price = price
        self.alcohol_level = alcohol_level

    def find_drink_by_name(self, name):
        if self.name == name:
            return name

    def find_alcohol_level(self, drink):
        return self.alcohol_level

