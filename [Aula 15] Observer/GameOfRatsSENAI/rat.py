from game import Game
from observer import Observer


class Rat:
    #def __init__(self, game: Game):
        #self.game = game
        #self.attack: int = 1
        #game.rat_enters.append(self.rat_enters)
        #game.notify_rat.append(self.notify_rat)

        #self.game.rat_enters(self)

    
        
        
        
    def rat_enters(self, which_rat):
        print("entrou um rato")
        self.notify_rat(which_rat)
        self.game.rat_enters.remove(self.rat_enters)

    def notify_rat(self, which_rat):
        which_rat.attack = self.rat_enters
        self.game.notify_rat.remove(self.notify_rat)









    def __init__(self, observer: Observer) -> None:
        self.observer = observer
        self.attack: int = 1
        self.adicionar_rato()



    def adicionar_rato(self):
        self.observer.rats_observers.append(self)
        print("um rato entrou")
        self.observer.rats_notify.append(self)
        self.notificar()

    def notificar(self):
        for rat in self.observer.rats_notify:
            rat.attack = len(self.observer.rats_observers)
        
