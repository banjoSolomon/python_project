from Account.account_test import Account
from Account.bank_test import MyBank
if __name__ == "__main__":
    my_bank = MyBank()

    while True:
        print("\nWelcome to", my_bank.get_name())
        print("1. Add Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Display Customer Count")
        print("6. Find Account")
        print("7. Display Accounts")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            try:
                account_number = int(input("Enter account number: "))
                new_account = Account(f"{first_name} {last_name}", "correct_pin", 0, account_number)
                my_bank.add_account(new_account)
                print("Account added successfully.")
            except ValueError:
                print("Invalid input. Account number must be an integer.")

        elif choice in ["2", "3"]:
            action = "Deposit" if choice == "2" else "Withdrawal"
            account_name = input(f"Enter account name for {action}: ")
            amount = input(f"Enter {action} amount: ")
            try:
                amount = float(amount)
                account = my_bank.find_account(account_name)
                if account:
                    if choice == "2":
                        my_bank.deposit(account, amount)
                    else:
                        my_bank.withdraw(account, amount)
                    print(f"{action} successful.")
                    print(f"New balance for {account.get_name()}: {account.get_balance('correct pin')}")
                else:
                    print("Account not found.")
            except ValueError:
                print("Invalid input. Amount must be a valid number.")

        elif choice == "4":
            sender_name = input("Enter sender account name: ")
            receiver_name = input("Enter receiver account name: ")
            amount = input("Enter transfer amount: ")
            try:
                amount = float(amount)
                sender = my_bank.find_account(sender_name)
                receiver = my_bank.find_account(receiver_name)
                if sender and receiver:
                    my_bank.transfer(sender, receiver, amount)
                    print("Transfer successful.")
                    print(f"New balance for {sender.get_name()}: {sender.get_balance('correct pin')}")
                    print(f"New balance for {receiver.get_name()}: {receiver.get_balance('correct pin')}")
                else:
                    print("Sender or receiver account not found.")
            except ValueError:
                print("Invalid input. Amount must be a valid number.")

        elif choice == "5":
            print("Customer Count:", my_bank.get_customer_count())

        elif choice == "6":
            account_name = input("Enter account name: ")
            account = my_bank.find_account(account_name)
            if account:
                print(f"Account found: {account.get_name()}")
            else:
                print("Account not found.")

        elif choice == "7":
            print("\nDisplaying Accounts:")
            for account in my_bank.get_accounts():
                print(f"Account Name: {account.get_name()}, Balance: {account.get_balance('correct pin')}")

        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")