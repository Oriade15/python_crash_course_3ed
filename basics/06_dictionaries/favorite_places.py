print("Favorite Places")

favorite_places_of_people = {
    'Oriade': 'Ilorin',
    'Femi': 'Ikeja',
    'Tolu': 'Ekiti',
    'Bolaji': 'Ibadan',
}

print("\nFavotrite places of some people")

for person, favorite_place in favorite_places_of_people.items():
    print(f"• {person}'s favorite place is {favorite_place}.")
