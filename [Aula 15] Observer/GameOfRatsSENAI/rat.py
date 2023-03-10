from game import Game


class Rat:
    def __init__(self, game: Game, name):
        self.name = name
        self.game = game
        self.attack: int = 1
        #print(f"instanciei o {self.name}")
        game.rat_enters.append(self.rat_enters)
        game.notify_rat.append(self.notify_rat)

        self.game.rat_enters(self)

    def rat_enters(self, which_rat):
        if self == which_rat:
            #print(f"rat_enters --- {self.name} é igual {which_rat.name}")
            if which_rat.attack == 1:
                #print("Entrou o primeiro rato no game")
                return
        else:
            #print(f"rat_enters --- {self.name} não é igual {which_rat.name}")
            if which_rat.attack == 1:
                #print("entrou um novo rato no game")
                self.game.notify_rat(which_rat)

    def notify_rat(self, which_rat):
        if self == which_rat:
            #print(f"--- notify_rat --- {self.name} é igual {which_rat.name}")
            return
        
        #print(f"--- notify_rat --- {self.name} não é igual {which_rat.name}")
        self.attack += 1
        #print(f"o {self.name}: attack +1")
        which_rat.attack = self.attack
        #print(f"o {which_rat.name}: = {self.attack}")
        
        