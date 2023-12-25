import json
from datetime import datetime
import pandas as pd

class Logger:
    def log_event(self, event):
        """Log an event with a timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('log.txt', 'a') as log_file:
            log_file.write(f"{timestamp}: {event}\n")

# The Logger class provides a simple logging mechanism with a timestamp.

class AccountManager(Logger):
    accounts = []  # Shared list to store account data

    def __init__(self):
        super().__init__()
        self.accounts = self.load_data()

    def load_data(self):
        """Load account data from a JSON file."""
        try:
            with open('accounts.json', 'r') as file:
                data = file.read()
                if data:
                    return json.loads(data)
                else:
                    return []
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []

    def save_data(self):
        """Save account data to a JSON file."""
        with open('accounts.json', 'w') as file:
            json.dump(self.accounts, file, indent=2)

# The AccountManager class handles loading and saving account data to/from a JSON file.

class AccountCreation(AccountManager):
    def create_account(self, bank_name, account_number, card_number, initial_balance):
        """Create a new account and save it."""
        account = {
            'bank_name': bank_name,
            'account_number': account_number,
            'card_number': card_number,
            'balance': initial_balance,
            'transactions': [],
            'frequent_activities': {'income': [], 'expense': []}
        }
        self.accounts.append(account)
        self.save_data()
        self.log_event(f"New account created: {account}")
        print(f"Account created successfully: {account}")
        return account  # Return the created account

# The AccountCreation class extends AccountManager to add functionality for creating accounts.

class AccountTransaction(AccountManager):
    def add_transaction(self, account, amount, transaction_type, category, description):
        """Add a transaction to an account."""
        transaction = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': amount,
            'type': transaction_type,
            'category': category,
            'description': description
        }
        account['transactions'].append(transaction)
        if transaction_type == 'Expense':
            account['balance'] -= amount
        elif transaction_type == 'Income':
            account['balance'] += amount
        self.save_data()
        self.log_event(f"Transaction added to account {account['account_number']}: {transaction}")
        print(f"Transaction added successfully: {transaction}")

# The AccountTransaction class extends AccountManager to add functionality for adding transactions.

class AccountDisplay(AccountManager):
    def display_account_info(self, account_number, bank_name):
        """Display account information."""
        print(f"Searching for account: {account_number}, {bank_name}")
        for account in self.accounts:
            print(f"Checking account: {account['account_number']}, {account['bank_name']}")
            if account['account_number'] == account_number and account['bank_name'] == bank_name:
                df_account_info = pd.DataFrame([account])
                print("Account Information:")
                print(df_account_info)
                return account
        print("Account not found.")
        return None

    def display_transactions(self, account):
        """Display transaction history for an account."""
        if account['transactions']:
            df_transactions = pd.DataFrame(account['transactions'])
            print("Transaction History:")
            print(df_transactions)
        else:
            print("No transactions found.")

    def display_frequent_activities(self, account, activity_type):
        """Display frequent activities for an account."""
        if account['frequent_activities'][activity_type]:
            df_activities = pd.DataFrame(account['frequent_activities'][activity_type])
            print(f"Frequent {activity_type.capitalize()} Activities:")
            print(df_activities)
        else:
            print(f"No frequent {activity_type} activities found.")

# The AccountDisplay class extends AccountManager to add functionality for displaying account information.

# Initialize account_display outside the loop
account_display = AccountDisplay()

# Example usage in a loop
account_info = None

while True:
    # Displaying options for the user to interact with the banking system
    print("\nOptions:")
    print("1. Create Account")
    print("2. Display Account Info")
    print("3. Add Transaction")
    print("4. Display Transactions")
    print("5. Display Frequent Activities")
    print("6. Add Frequent Activity")
    print("7. Exit")

    # Taking user input for their choice
    choice = input("Enter your choice: ")

    # Handling user choices and interacting with the corresponding classes
    if choice == "1":
        # Creating an account
        account_creation = AccountCreation()
        bank_name = input("Enter bank name: ")
        account_number = input("Enter account number: ")
        card_number = input("Enter card number: ")
        initial_balance = float(input("Enter initial balance: "))
        account_info = account_creation.create_account(bank_name, account_number, card_number, initial_balance)

    elif choice == "2":
        # Displaying account information
        account_number = input("Enter account number: ")
        bank_name = input("Enter bank name: ")
        account_info = account_display.display_account_info(account_number, bank_name)

    # ... (similar handling for other choices)

    elif choice == "7":
        # Exiting the program
        print("Exiting the program. Goodbye!")
        break

    else:
        # Handling invalid choices
        print("Invalid choice. Please enter a valid option.")

