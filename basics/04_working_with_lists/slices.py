print("Slices")

odd_numbers_from_1_to_20 = range(1, (20+1), 2)

print("\nOdd numbers from one to twenty: ")
for number in odd_numbers_from_1_to_20:
    print(f"• {number}")

# First 3 numbers
print("\nThe first 3 odd numbers from one to twenty: ")
for number in odd_numbers_from_1_to_20[:3]:
    print(f"• {number}")

# Middle 3 Numbers
print("\nThe 3 middle odd numbers from one to twenty: ")
# Find the index of the first number from the 3 middle items
first_index_of_middle_3 = int((len(odd_numbers_from_1_to_20)-3)/2)
for number in odd_numbers_from_1_to_20[
    first_index_of_middle_3:first_index_of_middle_3+3]:
    print(f"• {number}")

# Last 3 Numbers

print("\nThe last 3 odd numbers from one to twenty: ")
for number in odd_numbers_from_1_to_20[-3:]:
    print(f"• {number}")