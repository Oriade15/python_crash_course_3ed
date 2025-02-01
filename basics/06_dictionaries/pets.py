print("Pets")

pets = [
    {
        'kind': 'Cat',
        'owner': 'Oriade',
    },
    {
        'kind': 'Mice',
        'owner': 'Femi',
    },
    {
        'kind': 'Guinea Pig',
        'owner': 'Dapo',
    },
]

print("\nPets Info")

pet_index = 1
for pet in pets:
    print(f"• Pet {pet_index}")
    print(f"\t• Kind: {pet['kind']}")
    print(f"\t• Owner: {pet['owner']}")
    pet_index += 1
