print("Hello Admin")

usernames = ['john', 'kitty', 'admin', 'ninja', 'dev']

print("\nLogging Users in .....")
for username in usernames:
    if username == 'admin':
        print(f"• Hello {username.title()}, would you like to see a status report?")
    else:
        print(f"• Hello {username}, thank you for logging in again.")

print("\nRemoving Users .....")
for value in range(0, len(usernames)):
    usernames.pop()

print("\nLogging Users in .....")
if not usernames:
    print("\tWe need to find some users!")


