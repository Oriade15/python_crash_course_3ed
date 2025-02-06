print("Users\n")

class User:

    def __init__(self, first_name, last_name, username, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email_address = email_address

    def describe(self):
        print("Desribing User")
        print(f" • First Name: {self.first_name}")
        print(f" • Last Name: {self.last_name}")
        print(f" • Username: {self.username}")
        print(f" • Email Address: {self.email_address}\n")

    def greet(self):
        print(f"Hello {self.first_name}, What can I do for you today.")


users = [
    User("Oriade", "Ishola", "Oriade15", "isholaoriade15@gmail.com"),
    User("Abdulquadri", "Oriade", "Abdulquadri6229", "oriadeabdul17@gmail.com"),
    User("Abdulquadri", "Ishola", "AbdulQ", "isholaabdul19@gmail.com"),
]

for user in users:
    user.describe()

print("Greeting Users\n")
for user in users:
    user.greet()