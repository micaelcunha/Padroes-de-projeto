from event import Event


class Pessoa:
    def __init__(self, idade: int = 0) -> None:
        self._idade = idade
        self.eventos = Event()
        
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, value: int):
        if self._idade == value:
            return
        
        self._idade = value
        self.eventos("idade", value)
        