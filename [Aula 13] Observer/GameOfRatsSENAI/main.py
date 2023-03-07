from game import Game
from rat import Rat


def test_single_rat():
    game = Game()
    rat = Rat(game)
    print(f"rat 1: {rat.attack} should equal 1.")


def test_two_rats():
    game = Game()
    rat = Rat(game)
    rat2 = Rat(game)
    print(f"rat 1: {rat.attack} should equal 2.")
    print(f"rat 2: {rat2.attack} should equal 2.")


test_single_rat()
print("\n")
test_two_rats()