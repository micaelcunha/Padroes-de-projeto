from game import Game


class Rat:
    def __init__(self, game: Game):
        self.game = game
        self.attack: int = 1

    def rat_enters(self, which_rat):
        pass

    def notify_rat(self, which_rat):
        pass