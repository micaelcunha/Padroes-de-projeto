from abc import ABC

from creature import Creature


class CardGame(ABC):
    def __init__(self, creatures: list[Creature]) -> None:
        self.creatures = creatures

    def combat(self, creature_1: Creature, creature_2: Creature) -> Creature:
        self.hit(creature_1, creature_2)
        self.hit(creature_2, creature_1)

        first_alive: bool = creature_1.health > 0
        second_alive: bool = creature_2.health > 0

        if first_alive == second_alive:
            return Creature("Empate", -1, -1)

        if first_alive:
            return creature_1
        else:
            return creature_2

    def hit(self, attacker: Creature, defender: Creature):
        pass
