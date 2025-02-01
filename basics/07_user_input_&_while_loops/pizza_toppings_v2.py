print("Pizza Toppings (version 2)")

print("\nWelcome to Python Pizzeria" + 
    "\nKindly enter the pizza toppings you want.\n")

# • Use an active variable to control how long the loop runs.
is_program_active = True

while is_program_active:
    pizza_topping = input("\nPizza topping (To exit, enter 'x'): ")

    if pizza_topping == 'x':
        print("Exiting ...")
        is_program_active = False
    else:
        print(f"• Adding {pizza_topping} to your requested toppings.")
