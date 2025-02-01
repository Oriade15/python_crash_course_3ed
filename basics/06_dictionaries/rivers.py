print("Rivers")

rivers_and_countries = {
    'nile': 'egypt',
    'niger': 'nigeria',
    'congo': 'democratic republic of congo'
}

print("\nRivers and the countries they run through")

for river, country in rivers_and_countries.items():
    print(f"• The {river.title()} runs through {country.title()}.")

print("\nList of rivers")

for river in rivers_and_countries.keys():
    print(f"• {river.title()}")

print("\nList of countries rivers run through")

for country in rivers_and_countries.values():
    print(f"• {country.title()}")
