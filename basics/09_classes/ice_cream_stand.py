print("Ice Cream Stand")


class Restaurant:
    
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f"This is the {self.name} restaurant.")
        print(f"We are a {self.cuisine_type} restaurant.\n")

    def open(self):
        print("We are now open.\n") 


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"Here are the flavours we have at {self.name}: ")
        for flavor in self.flavors:
            print(f" • {flavor}")


new_ice_cream_stand = IceCreamStand("Ben & Jerry's", "ice cream", 
    ['Vanilla', 'Chocolate', 'Strawberry', 'Banana', 'Mango'])

new_ice_cream_stand.display_flavors()

