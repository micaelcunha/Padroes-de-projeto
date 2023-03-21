from creature import Creature
from permanent_damage_card_game import PermanentDamageCardGame
from temporary_damage_card_game import TemporaryDamageCardGame


class Facede:
    def 
# Case permanent_damage_card_game
# creature_elf = Creature("Elf", 1, 2)
# creature_orc = Creature("Orc", 1, 3)

# Case temporary_damage_card_game
creature_elf = Creature("Elf", 1, 1)
creature_orc = Creature("Orc", 2, 2)


creatures: list[Creature] = []

creatures.append(creature_elf)
creatures.append(creature_orc)

# permanent_damage_card_game = PermanentDamageCardGame(creatures)

# primeiro_round = permanent_damage_card_game.combat(creature_elf, creature_orc)
# print(primeiro_round.name)
# segundo_round = permanent_damage_card_game.combat(creature_elf, creature_orc)
# print(segundo_round.name)

temporary_damage_card_game = TemporaryDamageCardGame(creatures)

creature_elf.status()
creature_orc.status()

primeiro_round = temporary_damage_card_game.combat(creature_elf, creature_orc)
print(f"Vencedor é {primeiro_round.name}")

creature_elf.status()
creature_orc.status()