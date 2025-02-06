print("Login Attempts\n")


class User:

    def __init__(self, first_name, last_name, username, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email_address = email_address
        self.login_attempts = 0

    def describe(self):
        print("Desribing User")
        print(f" • First Name: {self.first_name}")
        print(f" • Last Name: {self.last_name}")
        print(f" • Username: {self.username}")
        print(f" • Email Address: {self.email_address}\n")

    def greet(self):
        print(f"Hello {self.first_name}, What can I do for you today.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts  = 0


new_user =  User("Oriade", "Ishola", "Oriade15", "isholaoriade15@gmail.com")

for value in range(0, 5):
    print(f" • Logging in '{new_user.username}'")
    new_user.increment_login_attempts()

print(f"\n{new_user.username}, it seems like you logged in {new_user.login_attempts} time(s).")

print("\nReseting your login attempts ...")
new_user.reset_login_attempts()

print(f"\nYour login attempts has been reset to {new_user.login_attempts}.")

