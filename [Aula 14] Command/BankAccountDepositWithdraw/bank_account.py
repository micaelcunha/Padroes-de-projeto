class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance: int = 0) -> None:
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f"Deposited = {amount}, balance = {self.balance}")

    def withdraw(self, amount: int) -> None:
        if (self.balance - amount >= BankAccount.OVERDRAFT_LIMIT):
            self.balance -= amount
            print(f"Withdrew = {amount}, balance = {self.balance}")
            return True
        
        return False

    def __str__(self) -> str:
        return f"Balance = {self.balance}"
