print("Pizza Toppings (version 3)")

print("\nWelcome to Python Pizzeria" + 
    "\nKindly enter the pizza toppings you want.\n")

# • Use a conditional test in the while statement to stop the loop.

while True:
    pizza_topping = input("\nPizza topping (To exit, enter 'x'): ")

    if pizza_topping == 'x':
        print("Exiting ...")
        break
    else:
        print(f"• Adding {pizza_topping} to your requested toppings.")
