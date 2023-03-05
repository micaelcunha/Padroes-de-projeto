from action import Action


class Command:
    def __init__(self, action: Action, amount: int):
        self.action = action
        self.amount = amount
        self.success = False

    