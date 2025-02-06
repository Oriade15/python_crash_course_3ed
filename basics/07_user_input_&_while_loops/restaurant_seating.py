print("Restaurant Seating")

print("\nWelcome to Python Restaurant!" + 
    "\nKindly provide number of people in your group" + 
    " so we can book you a table reservation.")

member_count = int(input("\nNumber of Members: "))

print("\nChecking if we can book a table reservation for you .....")
if member_count > 8:
    print("\nIt seems like we can't book you a table reservation now," + 
        " so you'll have to wait a bit.\nThanks for your patience.")
else:
    print("\nYour Table is ready.")