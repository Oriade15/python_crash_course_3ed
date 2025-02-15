from pathlib import Path
import json


def get_stored_user_info(path):
    """ Get stored username if available. """
    if path.exists():
        user_info = json.loads(path.read_text())
        return user_info
    else:
        return None


def store_user_info(path, user_info):
    """ Stores user's info """
    path.write_text(json.dumps(user_info))


def get_user_info():
    """ Prompt User for info. """
    print("\nEnter your info so we can remember you next time.\n")
    user_info = {}
    user_info['username'] = input("Username: ")
    user_info['email'] = input("Email Address: ")
    user_info['first_name'] = input("First Name: ")
    user_info['last_name'] = input("Last Name: ")

    return user_info


def display_user_info(user_info):
    """ Displays User Info """
    print(f"\nWelcome back, {user_info['username']}!")
    print("\nHere are your details: ")
    print(f" • Username: {user_info['username']}")
    print(f" • Email address: {user_info['email']}")
    print(f" • First Name: {user_info['first_name']}")
    print(f" • Last Name: {user_info['last_name']}")


def greet_user():
    """Greet the user by name."""
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)
    if user_info:
        display_user_info(user_info)
    else:
        user_info = get_user_info()
        store_user_info(path, user_info)
        print(f"\nWe'll remember you when you come back, {user_info['username']}!")


print("User Dictionary")

greet_user()