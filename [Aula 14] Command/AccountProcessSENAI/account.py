from action import Action
from command import Command


class Account:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if (amount <= self.balance):
            self.balance -= amount
            return True
        
        return False


    def process(self, command: Command):
        if(command.action == Action.DEPOSIT):
            self.deposit(command.amount)
            command.success = True
        elif(command.action == Action.WITHDRAW):
            command.success = (self.withdraw(command.amount))
