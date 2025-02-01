print("Cities")

cities_info = {
    'Ilorin': {
        'country': 'Nigeria',
        'approximate_population': 7000000,
        'fact': 'A home to tourist sites and natural resources'
    },
    'Mecca': {
        'country': 'Saudi Arabia',
        'approximate_population': 10000000,
        'fact': "A home to Ka'aba, a centre for Islam's pilgrimage"
    },
    'Cairo': {
        'country': 'Egypt',
        'approximate population': 15000000,
        'fact': 'A home to tourist sites and ancient egyptian history'
    },
}

print("\nCities Info")

for city, info in cities_info.items():
    print(f"• {city}: ")
    for key, value in info.items():
        print(f"\t• {key.title()}: {value}.")

