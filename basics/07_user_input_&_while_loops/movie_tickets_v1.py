print("Movie  Tickets (version 1)")

print("\nWelcome Python Cinema." + 
    "\nEnter your age to know the cost of your movie ticket.")

# • Use a break statement to exit the loop when the user enters a 'quit' value.

while True:
    age = input("\nAge (To exit, enter 'quit'): ")

    if age == 'quit':
        print("Exiting ...")
        break
    elif int(age) < 3:
        print("Checking ...")
        print("• Your movie ticket is free.")
    elif int(age) < 12:
        print("Checking ...")
        print("• Your movie ticket is costs $10.")
    else:
        print("Checking ...")
        print("• Your movie ticket is costs $15.")
