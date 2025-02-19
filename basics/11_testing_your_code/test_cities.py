from src.city_functions import format_city_description


def test_city_country():
    formatted_description = format_city_description('ilorin', 'nigeria')
    assert formatted_description == "Ilorin, Nigeria"


def test_city_country_population():
    formatted_description = format_city_description(
        'lagos', 'nigeria', 12000000)
    assert formatted_description  == "Lagos, Nigeria - Population: 12000000"
