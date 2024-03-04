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
        if account_sending.get_balance() >= amount:
            account_sending.withdraw(amount)
            account_receiving.deposit(amount)
        else:
            raise ValueError("Insufficient Funds For Transfer")

    def register_customer(self, first_name, last_name, account_number):
        self.customer_count += 1

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
        self.account = Account("UBA", "correct_pin", 0, 2347905)
        self.account_sending = Account("Banjo Solomon", "correct_pin", 0, 2347905)
        self.account_receiving = Account("Sam Kelly", "correct_pin", 0, 2347905)

    def test_bank_app_has_a_name(self):
        expected_name = "UBA"
        self.bank.set_name(expected_name)
        actual_name = self.bank.get_name()
        self.assertEqual(expected_name, actual_name)

    def test_account_are_in_a_list(self):
        account = Account("UBA", "correct_pin", 0, 2347905)
        self.bank.add_account(account)
        accounts = self.bank.get_accounts()
        self.assertIn(account, accounts)

    def test_that_account_is_zero(self):
        self.assertEqual(0, self.account.get_balance())

    def test_that_bank_can_deposit(self):
        initial_balance = self.account.get_balance()
        deposit_amount = 10_000
        self.bank.deposit(self.account, deposit_amount)
        expected_balance = initial_balance + deposit_amount
        self.assertEqual(expected_balance, self.account.get_balance())

    def test_bank_can_transfer(self):
        initial_sender_balance = self.account_sending.get_balance()
        deposit_amount = 10_000
        self.bank.deposit(self.account_sending, deposit_amount)
        initial_receiver_balance = self.account_receiving.get_balance()

        transfer_amount = 500
        self.bank.transfer(self.account_sending, self.account_receiving, transfer_amount)
        expected_receiver_balance = initial_receiver_balance + transfer_amount

        self.assertEqual(expected_receiver_balance, self.account_receiving.get_balance())

    def test_register_customer(self):
        first_name = "Sam"
        last_name = "Thomas"
        pin = "correct_pin"
        self.bank.register_customer(first_name, last_name, pin)
        self.assertEqual(1, self.bank.get_customer_count())

    def test_remove_account(self):
        solomon_account = Account("SolomonAccount", "correct_pin", 0, 2347905)
        self.bank.add_account(solomon_account)
        self.bank.remove_account(solomon_account)
        accounts = self.bank.get_accounts()
        self.assertNotIn(solomon_account, accounts)

    def test_to_find_account(self):
        kim_account = Account("KimAccount", "correct_pin", 0, 2347905)
        self.bank.add_account(kim_account)
        found_account = self.bank.find_account(kim_account.get_name())
        self.assertIsNotNone(found_account)
        self.assertEqual(kim_account, found_account)

    def test_for_withdraw(self):
        my_account = Account("myAccount", "correct_pin", 0, 2347905)
        initial_balance = 10_000
        my_account.deposit(initial_balance)
        self.bank.add_account(my_account)
        withdrawal_amount = 500
        self.bank.withdraw(my_account, withdrawal_amount)
        expected_balance = initial_balance - withdrawal_amount
        self.assertEqual(expected_balance, my_account.get_balance())
