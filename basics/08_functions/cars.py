print("Cars")


def print_car_info(car):
    """ Prints information about a car """
    print("\nHere's your car's info: ")
    for key, value in car.items():
        print(f" • {key.title()}: {value}")


def make_car(manufacturer, model, **properties):
    """ Makes and returns a car """
    properties['manufacturer']  = manufacturer
    properties['model'] = model

    return properties

car = make_car('Subaru', 'Outback', color='Blue', tow_package=True)

print_car_info(car)
