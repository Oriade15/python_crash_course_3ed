print("Deli")

sandwich_orders = [
    'tuna',
    'beans',
    'mayonaise',
    'tomato sauce'
]

finished_sandwiches = []

print("\nMaking Sandwiches for orders ...")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"• Making {current_sandwich} sandwich ...")

    finished_sandwiches.append(current_sandwich)

print("Done.")

print("\nHere's the list of sandwiches we made for the orders: ")
for sandwich in finished_sandwiches:
    print(f"• {sandwich.title()}")