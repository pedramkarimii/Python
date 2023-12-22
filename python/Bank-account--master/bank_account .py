class BankAccount:

    def __init__(self):
        self.accounts = {}
        self.minimum_balances = {}
        self.transaction_history = {}

    def create_account(self, name, initial_amount):
        if name in self.accounts:
            option = input(
                f"Account '{name}' already exists."
                f" Do you want to delete the previous account and create a new one?"
                f" (yes/no): ").lower()
            if option == 'yes':
                self._delete_account(name)
                self._create_account(name, initial_amount)
            else:
                print("Account creation canceled.")
        else:
            self._create_account(name, initial_amount)

    def _create_account(self, name, initial_amount):
        self.accounts[name] = initial_amount
        self.minimum_balances[name] = 0
        self.transaction_history[name] = [f"Account created with an initial deposit of ${initial_amount}"]

    def _delete_account(self, name):
        del self.accounts[name]
        del self.minimum_balances[name]
        del self.transaction_history[name]
        print(f"Account '{name}' deleted.")

    def deposit(self):
        name = input("Enter your account name: ")
        if name in self.accounts:
            amount = float(input("Enter the deposit amount: "))
            self.accounts[name] += amount
            self.transaction_history[name].append(f"Deposited ${amount} into the account.")
            print(f"Deposited ${amount} into the account for {name}. Current balance: ${self.accounts[name]}")
        else:
            create_new = input(f"Account '{name}' not found. Do you want to create a new account? (yes/no): ").lower()
            if create_new == 'yes':
                initial_amount = float(input("Enter the initial deposit amount: "))
                self.create_account(name, initial_amount)
            else:
                print("Deposit canceled. Account not found.")

    def withdraw(self):
        name = input("Enter your account name: ")
        if name in self.accounts:
            amount = float(input("Enter the withdrawal amount: "))
            if amount <= self.accounts[name] - self.minimum_balances[name]:
                self.accounts[name] -= amount
                self.transaction_history[name].append(f"Withdrew ${amount} from the account.")
                print(f"Withdrew ${amount} from the account for {name}. Current balance: ${self.accounts[name]}")
            else:
                print("Withdrawal canceled. Insufficient funds or below minimum balance.")
        else:
            print(f"Account '{name}' not found. Please enter the correct account name.")

    def transfer_money(self):
        sender_name = input("Enter your account name (sender): ")
        if sender_name in self.accounts:
            recipient_name = input("Enter the recipient's account name: ")
            if recipient_name in self.accounts:
                amount = float(input("Enter the transfer amount: "))
                if amount <= self.accounts[sender_name] - self.minimum_balances[sender_name]:
                    self.accounts[sender_name] -= amount
                    self.accounts[recipient_name] += amount
                    self.transaction_history[sender_name].append(f"Transferred ${amount} to {recipient_name}.")
                    print(f"Transferred ${amount} from {sender_name} to {recipient_name}.")
                else:
                    print("Transfer canceled. Insufficient funds or below minimum balance.")
            else:
                print(f"Recipient account '{recipient_name}' not found. Please enter the correct account name.")
        else:
            print(f"Sender account '{sender_name}' not found. Please enter the correct account name.")

    def set_minimum_balance(self):
        name = input("Enter your account name: ")
        if name in self.accounts:
            new_minimum_balance = float(input("Enter the new minimum balance: "))
            if new_minimum_balance <= self.accounts[name]:
                self.minimum_balances[name] = new_minimum_balance
                print(f"Minimum balance set to ${new_minimum_balance} for the account {name}.")
            else:
                print("Minimum balance cannot exceed the current account balance.")
        else:
            print(f"Account '{name}' not found. Please enter the correct account name.")

    def display_minimum_balance(self):
        name = input("Enter your account name: ")
        if name in self.accounts:
            print(f"Minimum balance for the account {name}: ${self.minimum_balances[name]}")
        else:
            print(f"Account '{name}' not found. Please enter the correct account name.")

    def print_account_summary(self):
        name = input("Enter your account name: ")
        if name in self.accounts:
            print(f"Account Summary for {name}: ")
            for activity in self.transaction_history[name]:
                print(f"{name}: {activity}")
        else:
            print(f"Account '{name}' not found. Please enter the correct account name.")

    def delete_account(self):
        name = input("Enter the account name you want to delete: ")
        if name in self.accounts:
            self._delete_account(name)
        else:
            print(f"Account '{name}' not found. Please enter the correct account name.")

    def show_all_transfers(self):
        print("All Transfer Activities:")
        for name, history in self.transaction_history.items():
            for activity in history:
                if "Transferred" in activity:
                    print(f"{name}: {activity}")


def main():
    account = BankAccount()

    while True:
        print(
            "\nOptions:\n1.Create account\n2.Deposit\n3.Withdraw\n"
            "4.Set minimum balance\n5.Display minimum balance\n"
            "6.Transfer money\n7.Print account summary\n8.Delete account\n"
            "9.Show all transfer activities\n10.Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            name = input("Enter your name: ")
            initial_amount = float(input("Enter the initial deposit amount: "))
            account.create_account(name, initial_amount)
        elif choice == '2':
            account.deposit()
        elif choice == '3':
            account.withdraw()
        elif choice == '4':
            account.set_minimum_balance()
        elif choice == '5':
            account.display_minimum_balance()
        elif choice == '6':
            account.transfer_money()
        elif choice == '7':
            account.print_account_summary()
        elif choice == '8':
            account.delete_account()
        elif choice == '9':
            account.show_all_transfers()
        elif choice == '10':
            print("Exiting the Bank Account. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")


if __name__ == "__main__":
    main()
