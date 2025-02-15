print("Addition")

print("Enter two numbers to find their sum.")

first_number = input("\nFirst number: ")
second_number = input("Second number: ")

try:
    sum = int(first_number) + int(second_number)
except ValueError:
    print("Oops! It seems like you entered a value that is not a number.")
else:
    print(f"{first_number} + {second_number} = {sum}.")
