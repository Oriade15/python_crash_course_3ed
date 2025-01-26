print("Ordinal Numbers")

numbers = range(1, 9+1)

for number in numbers:
    if number == 1:
        print(f"• {number}st")
    elif number == 2:
        print(f"• {number}nd")
    elif number == 3:
        print(f"• {number}rd")
    else:
        print(f"• {number}th")