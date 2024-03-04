import unittest


class Account:
    pin_length = 4
    next_account_number = 1

    def __init__(self, account_name, pin, balance, account_number):
        self.account_number = Account.next_account_number
        self.balance = 0
        self.account_name = account_name
        self.pin = pin
        self.account_number = account_number

    def get_name(self):
        return self.account_name

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Funds Bro")

    def set_pin(self, expected_pin):
        if len(expected_pin) != Account.pin_length:
            raise ValueError("PIN should be a four digit number")


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account = Account("Banjo Solomon", "correct_pin", "balance", 45987290)
        self.account_sending = Account("John Sam", "correct_pin", "balance", 23567804)
        self.account_receiving = Account("Oliver Twist", "correct_pin", "balance", 234575)

    def test_the_name_of_the_account(self):
        self.assertEqual("Banjo Solomon", self.account.get_name())

    def test_to_check_balance(self):
        initial_balance = 10_000
        self.account.deposit(initial_balance)
        self.assertEqual(initial_balance, self.account.get_balance())

    def test_account_number(self):
        check_account = Account("Banjo Solomon", "correct_pin", "10_000", 45987290)
        account_number = check_account.get_account_number()
        self.assertEqual(45987290, account_number)

    def test_account_can_deposit(self):
        my_account = Account("Banjo Solomon", "correct_pin", "10_000", 45987290)
        initial_balance = my_account.get_balance()
        deposit_amount = 5000
        my_account.deposit(deposit_amount)
        expected_balance = initial_balance + deposit_amount
        self.assertEqual(expected_balance, my_account.get_balance())

    def test_account_can_withdraw(self):
        my_account = Account("UBA", "correct_pin", "10_000", 45987290)
        initial_balance = 10_000
        my_account.deposit(initial_balance)
        withdrawal_amount = 500
        my_account.withdraw(withdrawal_amount)
        expected_balance = initial_balance - withdrawal_amount
        self.assertEqual(expected_balance, my_account.get_balance())

    def test_to_check_amount_balance(self):
        initial_balance = 10_000
        self.account.deposit(initial_balance)
        self.assertEqual(initial_balance, self.account.get_balance())

    def test_invalid_withdrawal_amount(self):
        self.assertRaises(ValueError, self.account.withdraw, -500)
        self.assertRaises(ValueError, self.account.withdraw, 0)
        self.assertRaises(ValueError, self.account.withdraw, int("abc"))

