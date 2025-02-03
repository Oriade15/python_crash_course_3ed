print("Sandwiches")


def make_sandwich(*fillings):
    print("\nMaking Sandwiches ...")
    print("\nDone!")

    print("\n\tHere's the list of fillings in the sandwiches we just made: ")
    for filling in fillings:
        print(f"\t • {filling}")
    

make_sandwich('mayonaise', 'cabbage', 'peanut butter', 'strawberry jam',
    'tomatoes')

make_sandwich('cabbage', 'peanut butter', 'strawberry jam')

make_sandwich('mayonaise', 'tomatoes')