print("User Profile")


def print_profile(profile):
    print("\nHere's the profile you requested for printng: ")
    for key, value in profile.items():
        print(f"• {key.title()}: {value}")


def build_profile(first_name, last_name, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first name'] = first_name
    user_info['last name'] = last_name
    return user_info


user_profile = build_profile('Abdulquadri', 'Ishola',
    nationality='Nigerian',
    religion='Islam',
    school="University of Ilorin")

print_profile(user_profile)