class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def of_drinking_age(self, age):
        if age >= 18:
            return True

    def sell_a_drink(self, price, age):
        if self.of_drinking_age(age):
            self.till += price
            
    def refuse_service(self, customer):
        if customer.drunkenness > 10:
            return "Time to go home."
        else:
            return "Would you like another?"


