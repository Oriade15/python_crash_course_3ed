""" 8-5. Cities: Write a function called describe_city() that accepts the name of 
a city and its country. The function should print a simple sentence, such as 
Reykjavik is in Iceland. Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the 
default country """

print("Cities")

def describe_city(name, country='nigeria'):
    print(f"\n• {name.title()} is in {country.title()}.")

describe_city('ilorin')

describe_city('lagos')

describe_city('makkah', 'saudi arabia')
