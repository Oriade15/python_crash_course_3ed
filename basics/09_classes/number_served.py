print("Number Served\n")


class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe(self):
        print(f"This is the {self.name} restaurant.")
        print(f"We are a {self.cuisine_type} restaurant.\n")

    def open(self):
        print("We are now open.\n")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, value):
        self.number_served += value


new_restaurant = Restaurant("Dusty's Tasty Doughnuts", "fast food")

print(f"{new_restaurant.name} has served {new_restaurant.number_served} customer(s).\n")

new_restaurant.number_served += 3

print(f"{new_restaurant.name} has served {new_restaurant.number_served} customer(s).\n")

new_restaurant.set_number_served(5)

print(f"{new_restaurant.name} has served {new_restaurant.number_served} customer(s).\n")

new_restaurant.increment_number_served(9)

print(f"{new_restaurant.name} served {new_restaurant.number_served} customer(s) today.\n")
