print("Movie  Tickets (version 3)")

print("\nWelcome Python Cinema." + 
    "\nEnter your age to know the cost of your movie ticket.")


# • Use a conditional test in the while statement to stop the loop.
while True:
    age = input("\nAge (To exit, enter 'x'): ")

    if age == 'x':
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
