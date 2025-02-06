class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f"This is the {self.name} restaurant.")
        print(f"We are a {self.cuisine_type} restaurant.\n")

    def open(self):
        print("We are now open.\n")
