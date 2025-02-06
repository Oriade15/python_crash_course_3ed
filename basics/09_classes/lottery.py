from random import choice


def generate_list_with_unique_items_from_list(items_count, list):
    list_with_unique_items = []
    for value in range(0, items_count):
        item = choice(list)
        # Check To ensure that all generated items are unique
        while item in list_with_unique_items:
            item = choice(list)

        list_with_unique_items.append(item)

    return list_with_unique_items


print("Lottery\n")

choices = [
    1, 'x', 4, 'd', 25, 67, 's', 7, 8, 12, 'z', 16, 89, 10, 'q',
]

print("Any ticket matching the following code wins a prize.\n")

winning_code = generate_list_with_unique_items_from_list(4, choices)
print(f"Winning Code: {winning_code}\n")
