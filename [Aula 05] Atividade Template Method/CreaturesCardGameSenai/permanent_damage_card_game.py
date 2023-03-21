from card_game import CardGame
from creature import Creature


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature):
        defender.health -= attacker.attack
