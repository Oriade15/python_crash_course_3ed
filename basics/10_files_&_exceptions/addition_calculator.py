print("Addition Calculator")

print("Enter two numbers to find their sum.")

while True:
    first_number = input("\nFirst number: ")
    second_number = input("Second number: ")

    try:
        sum = int(first_number) + int(second_number)
    except ValueError:
        print("Oops! It seems like you entered a value that is not a number.")
    else:
        print(f"{first_number} + {second_number} = {sum}.")

    quit_choice = input("\nDo you want to continue\n" + 
        "Enter 'x' to quit or any other key to continue: ")
    if quit_choice == 'x':
        break
