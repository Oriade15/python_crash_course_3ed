def format_city_description(city, country, population=None):
    formatted_description = f"{city.title()}, {country.title()}"
    if population:
        formatted_description += f" - Population: {population}"
    return formatted_description
