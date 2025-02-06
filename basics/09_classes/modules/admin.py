# For handling import errors from files outside the 'modules' directory
if __name__ == '__main__':
    from user import User
else:
    from modules.user import User

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
