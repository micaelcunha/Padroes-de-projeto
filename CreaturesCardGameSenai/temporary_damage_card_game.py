from card_game import CardGame
from creature import Creature


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature):