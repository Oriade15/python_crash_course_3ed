print("Cubes")

# Using list comprehension
cubes_of_numbers_from_1_to_10 = [number**3 for number in range(1, (10+1))] 

for cube in cubes_of_numbers_from_1_to_10:
    print(f"• {cube}")