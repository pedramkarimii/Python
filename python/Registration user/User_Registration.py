import re


class UserRegistration:
    def __init__(self):
        self.user_data = []

    def is_valid_username(self, username):
        """Check if the username is valid."""
        return username.lower() not in ['maktab', 'python']

    def is_valid_username_length(self, username):
        """Check if the username meets the length requirement."""
        return len(username) >= 4

    def is_valid_password(self, password):
        """Check if the password meets the specified conditions."""
        password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%#*?&]{8,}$"
        return bool(re.match(password_regex, password))

    def is_valid_iranian_mobile(self, mobile_number):
        """Check if the mobile number has a valid Iranian format."""
        iranian_mobile_regex = r"09(1[0-9]|3[0-9]|2[0-9]|0[1-9]|9[0-9])[0-9]{7}$"
        return re.match(iranian_mobile_regex, mobile_number)

    def is_valid_iranian_phone(self, phone_number):
        """Check if the phone number has a valid Iranian format."""
        iranian_phone_regex = r'^0[1-9]\d{9}$'
        return re.match(iranian_phone_regex, phone_number)

    def validate_registration(self, username, password, mobile_number, phone_number):
        """Validate user registration based on specified rules."""
        return (
                self.is_valid_username(username)
                and self.is_valid_username_length(username)
                and self.is_valid_password(password)
                and self.is_valid_iranian_mobile(mobile_number)
                and self.is_valid_iranian_phone(phone_number)
        )

    def display_all_users(self):
        """Display details for all registered users."""
        if not self.user_data:
            print("No registered users.")
        else:
            for i, user in enumerate(self.user_data):
                print(f"User {i + 1} Details:")
                print(f"  Username: {user['username']}")
                print(f"  Password: {user['password']}")
                print(f"  Mobile Number: {user['mobile_number']}")
                print(f"  Phone Number: {user['phone_number']}")
                print()

    def run_registration_system(self):
        """Run the user registration system."""
        while True:
            print("\nOptions:")
            print("1. Register a user")
            print("2. Display allowed usernames")
            print("3. Display all user details")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                self.register_user()

            elif choice == '2':
                self.display_allowed_usernames()

            elif choice == '3':
                self.display_all_users()

            elif choice == '4':
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

    def register_user(self):
        """Register a new user."""
        username = input("Enter username: ")
        password = input("Enter password: ")
        mobile_number = input("Enter mobile number: ")
        phone_number = input("Enter phone number: ")

        if self.validate_registration(username, password, mobile_number, phone_number):
            self.user_data.append({
                'username': username,
                'password': password,
                'mobile_number': mobile_number,
                'phone_number': phone_number
            })
            print("User registration successful.")
        else:
            print("User registration failed. Please check the rules.")

    def display_allowed_usernames(self):
        """Display allowed usernames."""
        allowed_usernames = [user['username'] for user in self.user_data]
        print(f"Allowed Usernames: {allowed_usernames}")


if __name__ == "__main__":
    registration_system = UserRegistration()
    registration_system.run_registration_system()
