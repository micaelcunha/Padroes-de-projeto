class Creature:
    def __init__(self, name: str, attack: int, health: int) -> None:
        self.name = name
        self.health = health
        self.attack = attack

    def status(self) -> str:
        print(f"Name: {self.name}, Attack: {self.attack}, Health: {self.health}")
