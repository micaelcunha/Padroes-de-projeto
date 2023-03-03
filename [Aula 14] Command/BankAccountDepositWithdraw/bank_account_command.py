from action import Action
from bank_account import BankAccount
from command import Command


class BankAccountCommand(Command):
    def __init__(self, account: BankAccount, action: Action, amount: int) -> None:
        self.account = account
        self.action = action
        self.amount = amount
        self.success = None

    def invoke(self):
        if (self.action == Action.DEPOSIT):
            self.account.deposit(self.amount)
            self.success = True
        elif (self.action == Action.WITHDRAW):
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not (self.success):
            return

        if (self.action == Action.DEPOSIT):
            self.account.withdraw(self.amount)
        elif self.action == Action.WITHDRAW:
            self.account.deposit(self.amount)