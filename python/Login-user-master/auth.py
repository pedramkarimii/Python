from exceptoins import UsernameAlreadyExists, PasswordTooShort, InvalidUsername, InvalidPassword
from user import User


class Authenticator:
    def __init__(self):
        self.users = []

    def add_user(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        for user in self.users:
            if user.username == username:
                raise UsernameAlreadyExists("Username already exists.")

        if len(password) < 8:
            raise PasswordTooShort("Password should be at least 8 characters long.")

        new_user = User(username, password)
        self.users.append(new_user)

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for user in self.users:
            if user.username == username:
                if user.password == user._hash_password(password):
                    user.is_logged_in = True
                    print("Login successful.")
                    return
                else:
                    raise InvalidPassword("Invalid password.")
        raise InvalidUsername("I have not that username.Invalid username")

    def is_user_logged_in(self):
        username = input("Enter the username to check login status: ")
        for user in self.users:
            if user.username == username:
                print(f"{username} is {'logged in' if user.is_logged_in else 'not logged in'}.")
                return

        raise InvalidUsername("Invalid username.")


if __name__ == '__main__':
    authenticator = Authenticator()

    while True:
        print("\n1. Add User\n2. Login\n3. Check Login Status\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            try:
                authenticator.add_user()
                print("User successfully registered.")
            except (UsernameAlreadyExists, PasswordTooShort, InvalidUsername, InvalidPassword) as e:
                print(f"Error: {e}")

        elif choice == '2':
            try:
                authenticator.login()
            except (InvalidUsername, InvalidPassword) as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                authenticator.is_user_logged_in()
            except InvalidUsername as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("Goodbye...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
