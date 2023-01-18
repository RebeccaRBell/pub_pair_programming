class Food:
    def __init__(self, name, price, rejuvenation_level):
        self.name = name
        self.price = price
        self.rejuvenation_level = rejuvenation_level

    def eat_food(self, customer, food):
        customer.drunkenness -= food.rejuvenation_level