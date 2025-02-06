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


class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show(self):
        print("Here are your privileges: ")
        for privilege in self.privileges:
            print(f" • {privilege}")


class Admin(User):

    def __init__(self, first_name, last_name, username, email_address):
        super().__init__(first_name, last_name, username, email_address)
        self.privileges = Privileges()
