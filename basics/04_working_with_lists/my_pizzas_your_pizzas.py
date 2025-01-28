print("My Pizzas, Your Pizzas")

my_pizzas = ['Oblee', 'Dominoes', 'McDonalds']

friends_pizzas = my_pizzas[:]

my_pizzas.append('Spanish')

friends_pizzas.append('Mexican')

print("\nMy favourite pizzas are: ")
for pizza in my_pizzas:
    print(f"• {pizza}")

print("\nMy friend's favourite pizzas are: ")
for pizza in friends_pizzas:
    print(f"• {pizza}")
