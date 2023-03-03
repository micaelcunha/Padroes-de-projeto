from action import Action
from command import Command


class Account:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def process(self, command: Command):
        pass