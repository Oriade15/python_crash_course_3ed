print("Movie  Tickets (version 2)")

print("\nWelcome Python Cinema." + 
    "\nEnter your age to know the cost of your movie ticket.")

# • Use an active variable to control how long the loop runs.
is_program_active = True

while is_program_active:
    age = input("\nAge (To exit, enter 'x'): ")

    if age == 'x':
        print("Exiting ...")
        is_program_active = False
    elif int(age) < 3:
        print("Checking ...")
        print("• Your movie ticket is free.")
    elif int(age) < 12:
        print("Checking ...")
        print("• Your movie ticket is costs $10.")
    else:
        print("Checking ...")
        print("• Your movie ticket is costs $15.")
