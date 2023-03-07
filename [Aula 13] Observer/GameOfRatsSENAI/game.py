from event import Event


class Game:
    def __init__(self):
        self.rat_enters = Event()
        self.notify_rat = Event()