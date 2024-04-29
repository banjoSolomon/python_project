import unittest


class Account:
    pin_length = 4
    next_account_number = 1

    def __init__(self, account_name, pin, balance, account_number):
        self.account_number = Account.next_account_number
        self.balance = int(balance)
        self.account_name = account_name
        self.pin = pin
        self.account_number = account_number

    def get_name(self):
        return self.account_name

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def get_balance(self, pin):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid withdrawal")
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Funds Bro")

    def set_pin(self, expected_pin):
        if not expected_pin.isdigit() or len(expected_pin) != Account.pin_length:
            raise ValueError("PIN should be for-digit number")


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account = Account("Banjo Solomon", 2468, 0, 45987290)
        self.account_sending = Account("John Sam", 2468, 0, 23567804)
        self.account_receiving = Account("Oliver Twist", 2468, 0, 234575)

    def test_the_name_of_the_account(self):
        self.assertEqual("Banjo Solomon", self.account.get_name())

    def test_to_check_balance(self):
        initial_balance = 10_000
        self.account.deposit(initial_balance)
        self.assertEqual(initial_balance, self.account.get_balance(2468))

    def test_account_number(self):
        check_account = Account("Banjo Solomon", 2468, 0, 45987290)
        account_number = check_account.get_account_number()
        self.assertEqual(45987290, account_number)

    def test_account_can_deposit(self):
        initial_balance = self.account.get_balance(2468)
        deposit_amount = 5000
        self.account.deposit(deposit_amount)
        expected_balance = initial_balance + deposit_amount
        self.assertEqual(expected_balance, self.account.get_balance(2468))

    def test_account_can_withdraw(self):
        my_account = Account("UBA", 2468, 0, 45987290)
        initial_balance = 10_000
        my_account.deposit(initial_balance)
        withdrawal_amount = 500
        my_account.withdraw(withdrawal_amount)
        expected_balance = initial_balance - withdrawal_amount
        self.assertEqual(expected_balance, my_account.get_balance(2468))

    def test_to_check_amount_balance(self):
        initial_balance = 10_000
        self.account.deposit(initial_balance)
        self.assertEqual(initial_balance, self.account.get_balance(2468))

    def test_invalid_withdrawal_amount(self):
        self.assertRaises(ValueError, self.account.withdraw, -500)
        self.assertRaises(ValueError, self.account.withdraw, 0)

