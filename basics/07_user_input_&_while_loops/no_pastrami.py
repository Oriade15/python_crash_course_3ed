print("No Pastrami")

sandwich_orders = [
    'tuna',
    'pastrami',
    'beans',
    'pastrami',
    'mayonaise',
    'pastrami',
    'tomato sauce',
]

finished_sandwiches = []

print("\nMaking Sandwiches for orders except the Pastrami sandwich ...")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        print(f"• Declining a {current_sandwich} sandwich order ...")
    else:
        print(f"• Making {current_sandwich} sandwich ...")
        finished_sandwiches.append(current_sandwich)

print("Done.")

print("\nHere's the list of sandwiches we made for the orders: ")
for sandwich in finished_sandwiches:
    print(f"• {sandwich.title()}")
