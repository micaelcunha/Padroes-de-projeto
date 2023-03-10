from game import Game


class Rat:
    def __init__(self, game: Game):
        self.game = game
        self.attack: int = 1
        game.rat_enters.append(self.rat_enters)
        game.notify_rat.append(self.notify_rat)

        self.game.rat_enters(self)

    def rat_enters(self, which_rat):
        if self != which_rat:
            self.attack += 1
            self.game.notify_rat(which_rat)

    def notify_rat(self, which_rat):
        if self == which_rat:
            self.attack += 1
        
        