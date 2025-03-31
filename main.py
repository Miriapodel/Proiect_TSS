from decimal import Decimal

class BankAccount:
    def __init__(self, account_id, owner_name, balance=0.0, currency="RON"):
        assert isinstance(account_id, int) and account_id > 0, "Invalid account ID"
        assert isinstance(owner_name, str) and owner_name.strip(), "Invalid owner name"
        assert isinstance(balance, (int, float, Decimal)) and balance >= 0, "Invalid initial balance"
        assert currency in ("RON", "EUR", "USD"), "Unsupported currency"

        self.account_id = account_id
        self.owner_name = owner_name
        self.balance = Decimal(balance)
        self.currency = currency
        self.active = True
        self.transaction_limit = Decimal("10000.00")  # max per transaction

    def deposit(self, amount):
        if not self.active:
            raise Exception("Account is closed")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        if amount > self.transaction_limit:
            raise ValueError("Deposit exceeds transaction limit")

        self.balance += Decimal(amount)
        return self.balance

    def withdraw(self, amount):
        if not self.active:
            raise Exception("Account is closed")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.transaction_limit:
            raise ValueError("Withdraw exceeds transaction limit")
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= Decimal(amount)
        return self.balance

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount")
        if not self.active or not target_account.active:
            raise Exception("One of the accounts is inactive")
        if self.currency != target_account.currency:
            raise ValueError("Currency mismatch")
        if self.account_id == target_account.account_id:
            raise ValueError("Cannot transfer to the same account")

        self.withdraw(amount)
        target_account.deposit(amount)
        return True

    def get_balance(self):
        if not self.active:
            raise Exception("Account is closed")
        return float(self.balance)

    def close_account(self):
        if self.balance > 0:
            raise Exception("Withdraw remaining balance before closing account")
        self.active = False
        return True