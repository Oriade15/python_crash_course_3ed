print("Checking Usernames")

current_users = ['John', 'kitty', 'admin', 'Ninja', 'dev']

new_users = ['JOHN', 'boss', 'guru', 'ninja', 'knight']

usernames = current_users[:]
for value in range(0, len(usernames)):
    usernames[value] = usernames[value].lower()

print("\nChecking new users .....")

for new_user in new_users:
    if new_user.lower() in usernames:
        print(f"• Hey {new_user}, please enter different username, yours has already been taken.")
    else:
        print(f"• That's a nice username {new_user}, your username is available.")