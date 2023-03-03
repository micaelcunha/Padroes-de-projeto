from action import Action
from bank_account import BankAccount
from bank_account_command import BankAccountCommand

bank_account = BankAccount()
command = BankAccountCommand(bank_account, Action.DEPOSIT, 100)
command.invoke()
print(bank_account)

command.undo()
print(bank_account)
illegal_cmd = BankAccountCommand(bank_account, Action.WITHDRAW, 1000)
illegal_cmd.invoke()
print(bank_account)
illegal_cmd.undo()
print(bank_account)
