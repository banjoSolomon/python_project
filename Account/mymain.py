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
            account_number = int(input("Enter account number: "))
            new_account = Account(f"{first_name} {last_name}", "correct_pin", 0, account_number)
            my_bank.add_account(new_account)
            print("Account added successfully.")

        elif choice == "2":
            account_name = input("Enter account name: ")
            deposit_amount = float(input("Enter deposit amount: "))
            account = my_bank.find_account(account_name)
            if account:
                my_bank.deposit(account, deposit_amount)
                print("Deposit successful.")
                print(f"New balance for {account.get_name()}: {account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == "3":
            account_name = input("Enter account name: ")
            withdrawal_amount = float(input("Enter withdrawal amount: "))
            account = my_bank.find_account(account_name)
            if account:
                try:
                    my_bank.withdraw(account, withdrawal_amount)
                    print("Withdrawal successful.")
                    print(f"New balance for {account.get_name()}: {account.get_balance()}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Account not found.")

        elif choice == "4":
            sender_name = input("Enter sender account name: ")
            receiver_name = input("Enter receiver account name: ")
            amount = float(input("Enter transfer amount: "))
            sender = my_bank.find_account(sender_name)
            receiver = my_bank.find_account(receiver_name)
            if sender and receiver:
                try:
                    my_bank.transfer(sender, receiver, amount)
                    print("Transfer successful.")
                    print(f"New balance for {sender.get_name()}: {sender.get_balance()}")
                    print(f"New balance for {receiver.get_name()}: {receiver.get_balance()}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Sender or receiver account not found.")

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
                print(f"Account Name: {account.get_name()}, Balance: {account.get_balance()}")

        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
