from card_game import CardGame
from creature import Creature


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature):
        vida_inicial = defender.health
        defender.health -= attacker.attack
        if defender.health > 0:
            defender.health = vida_inicial