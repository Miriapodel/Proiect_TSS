import unittest
from decimal import Decimal
from main import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(1, "Alice", 1000)
        self.other_account = BankAccount(2, "Bob", 500)

    def test_deposit_valid(self):
        self.assertEqual(self.account.deposit(100), Decimal("1100"))

    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_deposit_limit(self):
        self.assertEqual(self.account.deposit(10000), Decimal("11000"))

    def test_deposit_above_limit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(10001)

    def test_withdraw_valid(self):
        self.assertEqual(self.account.withdraw(300), Decimal("700"))

    def test_withdraw_exact_balance(self):
        a = BankAccount(10, "X", 300)
        self.assertEqual(a.withdraw(300), Decimal("0"))

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)

    def test_withdraw_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-1)

    def test_withdraw_above_limit(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(20000)

    def test_transfer_valid(self):
        self.account.transfer(self.other_account, 200)
        self.assertEqual(self.account.balance, Decimal("800"))
        self.assertEqual(self.other_account.balance, Decimal("700"))

    def test_transfer_to_self(self):
        with self.assertRaises(ValueError):
            self.account.transfer(self.account, 50)

    def test_transfer_invalid_target_type(self):
        with self.assertRaises(TypeError):
            self.account.transfer("not an account", 50)

    def test_transfer_currency_mismatch(self):
        self.other_account.currency = "EUR"
        with self.assertRaises(ValueError):
            self.account.transfer(self.other_account, 50)

    def test_transfer_inactive_account(self):
        self.other_account.close_account()
        with self.assertRaises(Exception):
            self.account.transfer(self.other_account, 50)

    def test_get_balance_active(self):
        self.assertEqual(self.account.get_balance(), 1000.0)

    def test_get_balance_closed(self):
        self.account.balance = Decimal("0")
        self.account.close_account()
        with self.assertRaises(Exception):
            self.account.get_balance()

    def test_close_account_success(self):
        a = BankAccount(3, "C", 0)
        self.assertTrue(a.close_account())
        self.assertFalse(a.active)

    def test_close_account_with_balance(self):
        with self.assertRaises(Exception):
            self.account.close_account()

    def test_equality(self):
        acc2 = BankAccount(1, "Different Name")
        self.assertEqual(self.account, acc2)

    def test_str_format(self):
        self.assertIn("Alice", str(self.account))

if __name__ == '__main__':
    unittest.main()