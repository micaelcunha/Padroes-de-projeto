from account import Account
from action import Action
from command import Command

account = Account()

command = Command(Action.DEPOSIT, 100)
account.process(command)
print(account.balance)
print(command.success)

command = Command(Action.WITHDRAW, 50)
account.process(command)

print(account.balance)
print(command.success)

command.amount = 150
account.process(command)

print(account.balance)
print(command.success)