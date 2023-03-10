from game import Game


class Rat:
    def __init__(self, game: Game, name):
        self.name = name
        self.game = game
        self.attack: int = 1
        print(f"instanciei o {self.name}")
        game.rat_enters.append(self.rat_enters)
        game.notify_rat.append(self.notify_rat)

        self.game.rat_enters(self)

    def rat_enters(self, which_rat):
        if self == which_rat:
            print(f"rat_enters --- {self.name} é igual {which_rat.name}")
            print("Um rato entrou no game")
        else:
            print(f"rat_enters --- {self.name} não é igual {which_rat.name}")
            print("entrou um novo rato no game")
            which_rat.attack = self.attack + 1
            self.game.notify_rat(which_rat)

    def notify_rat(self, which_rat):
        if self == which_rat:
            print(f"--- notify_rat --- {self.name} é igual {which_rat.name}")
            #which_rat.attack += 1
            #print(f"{which_rat.name}: attack +1")
        else:
            print(f"--- notify_rat --- {self.name} não é igual {which_rat.name}")
            self.attack = which_rat.attack
            return
            #print(f"{self.name}: attack +1")
        
        
        
    #def rat_enters(self, which_rat):
     #   print("entrou um rato")
      #  self.notify_rat(which_rat)
       # self.game.rat_enters.remove(self.rat_enters)

    #def notify_rat(self, which_rat):
     #   which_rat.attack
      #  self.game.notify_rat.remove(self.notify_rat)









    #def __init__(self, observer: Observer) -> None:
        #self.observer = observer
        #self.attack: int = 1
        #self.adicionar_rato()



    #def adicionar_rato(self):
     #   self.observer.rats_observers.append(self)
      #  print("um rato entrou")
       # self.notificar()
        #self.observer.rats_notify.append(self)

    #def notificar(self):
     #   for rat in self.observer.rats_notify:
      #      rat.attack += 1
