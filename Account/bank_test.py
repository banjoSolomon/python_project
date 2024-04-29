import unittest

from Account.account_test import Account


class MyBank:

    def __init__(self):
        self.customer_count = 0
        self.accounts = []
        self.name = "UBA"

    def set_name(self, expected_name):
        self.name = expected_name

    def get_name(self):
        return self.name

    def add_account(self, account):
        self.accounts.append(account)

    def get_accounts(self):
        return self.accounts

    def deposit(self, account, deposit_amount):
        account.deposit(deposit_amount)

    def transfer(self, account_sending, account_receiving, amount):
        if account_sending.get_balance("correct pin") >= amount:
            account_sending.withdraw(amount)
            account_receiving.deposit(amount)
        else:
            raise ValueError("Insufficient Funds For Transfer")

    def register_customer(self, first_name, last_name, pin):
        self.customer_count += 1
        new_account = Account(first_name, last_name, 0, pin)
        self.add_account(new_account)

    def get_customer_count(self):
        return self.customer_count

    def remove_account(self, account):
        self.accounts.remove(account)

    def find_account(self, account_name):
        for account in self.accounts:
            if account.get_name() == account_name:
                return account
        return None

    def withdraw(self, my_account, withdrawal_amount):
        my_account.withdraw(withdrawal_amount)


class TestBankApp(unittest.TestCase):
    def setUp(self):
        self.bank = MyBank()
        self.account = Account("UBA", 234, 0, 2347905)
        self.account_sending = Account("Banjo Solomon", 234, 0, 2347905)
        self.account_receiving = Account("Sam Kelly", 234, 0, 2347905)

    def test_bank_app_has_a_name(self):
        expected_name = "UBA"
        self.bank.set_name(expected_name)
        actual_name = self.bank.get_name()
        self.assertEqual(expected_name, actual_name)

    def test_account_are_in_a_list(self):
        account = Account("UBA", 234, 0, 2347905)
        self.bank.add_account(account)
        accounts = self.bank.get_accounts()
        self.assertIn(account, accounts)

    def test_that_account_is_zero(self):
        self.assertEqual(0, self.account.get_balance(234))

    def test_that_bank_can_deposit(self):
        initial_balance = self.account.get_balance(234)
        deposit_amount = 10_000
        self.bank.deposit(self.account, deposit_amount)
        expected_balance = initial_balance + deposit_amount
        self.assertEqual(expected_balance, self.account.get_balance(234))

    def test_that_bank_can_check_balance_with_pin(self):
        initial_balance = self.account.get_balance(234)
        deposit_amount = 20_000
        self.bank.deposit(self.account, deposit_amount)
        expected_balance = initial_balance + deposit_amount
        self.assertEqual(expected_balance, self.account.get_balance(234))

    def test_to_withdraw_with_invalid_pin(self):
        initial_balance = self.account.get_balance(211)
        deposit_amount = 20_000
        self.bank.deposit(self.account, deposit_amount)
        expected_balance = initial_balance + deposit_amount
        withdrawal_amount = 5_000
        self.bank.withdraw(self.account, withdrawal_amount, pin=234)
        expected_balance = initial_balance - withdrawal_amount
        self.assertEqual(expected_balance, self.account.get_balance(211))

    def test_bank_can_transfer(self):
        initial_sender_balance = self.account_sending.get_balance(234)
        deposit_amount = 10_000
        self.bank.deposit(self.account_sending, deposit_amount)
        initial_receiver_balance = self.account_receiving.get_balance(234)

        transfer_amount = 500
        self.bank.transfer(self.account_sending, self.account_receiving, transfer_amount)
        expected_receiver_balance = initial_receiver_balance + transfer_amount

        self.assertEqual(expected_receiver_balance, self.account_receiving.get_balance(234))

    def test_register_customer(self):
        initial_customer_count = self.bank.get_customer_count()
        first_name = "Sam"
        last_name = "Thomas"
        pin = "correct_pin"
        self.bank.register_customer(first_name, last_name, pin)
        updated_customer_count = self.bank.get_customer_count()
        self.assertEqual(initial_customer_count + 1, updated_customer_count)

        found_account = self.bank.find_account(f"{first_name}{last_name}")
        self.assertIsNotNone(found_account)

        self.assertEqual(first_name, found_account.get_first_name())
        self.assertEqual(last_name, found_account.get_last_name())
        self.assertEqual(pin, found_account.get_pin())
        self.assertEqual(0, found_account.get_balance())

    def test_remove_account(self):
        solomon_account = Account("SolomonAccount", 234, 0, 2347905)
        self.bank.add_account(solomon_account)
        self.bank.remove_account(solomon_account)
        accounts = self.bank.get_accounts()
        self.assertNotIn(solomon_account, accounts)

    def test_to_find_account(self):
        kim_account = Account("KimAccount", 234, 0, 2347905)
        self.bank.add_account(kim_account)
        found_account = self.bank.find_account(kim_account.get_name())
        self.assertIsNotNone(found_account)
        self.assertEqual(kim_account, found_account)

    def test_for_withdraw(self):
        my_account = Account("myAccount", 234, 0, 2347905)
        initial_balance = 10_000
        my_account.deposit(initial_balance)
        self.bank.add_account(my_account)
        withdrawal_amount = 500
        self.bank.withdraw(my_account, withdrawal_amount)
        expected_balance = initial_balance - withdrawal_amount
        self.assertEqual(expected_balance, my_account.get_balance(234))
