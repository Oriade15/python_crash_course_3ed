print("Multiples of Ten")

print("\nEnter a number let's see if it's multiple of 10.")

number = int(input("\nNumber: "))

print("\nChecking ...\n")
if number % 10 != 0:
    print(f"The number {number} is'nt a multiple of ten.")
else:
    print(f"The number {number} is a multiple of ten.")
