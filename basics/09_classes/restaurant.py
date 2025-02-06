print("Restaurant")

class Restaurant:
    
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f"This is the {self.name} restaurant.")
        print(f"We are a {self.cuisine_type} restaurant.\n")

    def open(self):
        print("We are now open.\n")


new_restaurant = Restaurant("Dusty's Tasty Doughnuts", "fast food")

print("\nDisplaying the attributes of our new restauraant")
print(f" • {new_restaurant.name}")
print(f" • {new_restaurant.cuisine_type}")

new_restaurant.describe()

new_restaurant.open()