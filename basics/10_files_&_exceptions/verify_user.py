from pathlib import Path
import json


def get_stored_username(path):
    """ Get stored username if available. """
    if path.exists():
        username = json.loads(path.read_text())
        return username
    else:
        return None


def store_username(path, username):
    """ Stores user's info """
    path.write_text(json.dumps(username))


def get_new_username():
    """ Prompt User for info. """
    print("\nEnter your username so we can remember you next time.")
    username = input("Username: ")

    return username


def verify_username(username):
    """ Verifies username """
    print(f"\nIs '{username}' your username? ")
    is_username  = input("Enter 'y' for yes & any other key for no: ")
    if is_username == 'y':
        return True
    else:
        return False


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        if verify_username(username):
            print(f"Welcome Back {username}!")
        else:
            username = get_new_username()
            store_username(path, username)
            print(f"\nWe'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        store_username(path, username)
        print(f"\nWe'll remember you when you come back, {username}!")

print("Verify User")

greet_user()