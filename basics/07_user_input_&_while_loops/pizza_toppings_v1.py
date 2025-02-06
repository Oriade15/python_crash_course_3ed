print("Pizza Toppings (version 1)")

print("\nWelcome to Python Pizzeria" + 
    "\nKindly enter the pizza toppings you want.\n")

# • Use a break statement to exit the loop when the user enters a 'quit' value.
while True:
    pizza_topping = input("\nPizza topping (To exit, enter 'quit'): ")

    if pizza_topping == 'quit':
        print("Exiting ...")
        break
    else:
        print(f"• Adding {pizza_topping} to your requested toppings.")
