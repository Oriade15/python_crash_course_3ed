print("Favorite numbers 2")

favorite_numbers_of_people = {
    'Oriade': [
        23, 24, 25,
    ],
    'Temi': [
        90, 13, 14,
    ],
    'Bolu': [
        4, 9, 16, 25,
    ],
    'Victor': [
        11, 13, 17, 19
    ],
    'Tola': [
        17, 34, 51, 68, 85
    ]
}

print("\nFavorite numbers of a set of people")

for person in favorite_numbers_of_people.keys():
    print(f"• {person}: ")
    for number in favorite_numbers_of_people[person]:
        print(f"\t• {number}")
