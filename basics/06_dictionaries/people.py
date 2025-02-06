print("People")

people = [
    {
        'first_name': 'Abdulquadri',
        'middle_name': 'Oriade',
        'last_name': 'Ishola',
        'age': 19,
        'city': 'Ilorin'
    },
    {
        'first_name': 'Baldwin',
        'middle_name': 'Femi',
        'last_name': 'Okeowo',
        'age': 23,
        'city': 'Ibadan'
    },
    {
        'first_name': 'Abdulhafeez',
        'middle_name': 'Dapo',
        'last_name': 'Oluwaseun',
        'age': 25,
        'city': 'Oshodi'
    },
]

print("\nPeople Info")

person_index = 1 
for person in people:
    print(f"• Person {person_index}")
    print(f"\t• First name: {person['first_name']}")
    print(f"\t• Middle name: {person['middle_name']}")
    print(f"\t• Last name: {person['last_name']}")
    print(f"\t• Age: {person['age']}")
    print(f"\t• City: {person['city']}")
    person_index += 1