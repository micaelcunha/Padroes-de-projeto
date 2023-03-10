from game import Game
from rat import Rat


def test_single_rat():
    game = Game()
    rat = Rat(game, "rato1")
    print(f"rat 1: {rat.attack} should equal 1.")


def test_two_rats():
    game = Game()
    rat = Rat(game, "rato1")
    rat2 = Rat(game, "rato2")

    print(f"rat 1: {rat.attack} should equal 2.")
    print(f"rat 2: {rat2.attack} should equal 2.")

def test_three_rats():
    game = Game()
    rat = Rat(game, "rato1")
    rat2 = Rat(game, "rato2")
    rat3 = Rat(game, "rato3")

    print(f"rat 1: {rat.attack} should equal 3.")
    print(f"rat 2: {rat2.attack} should equal 3.")
    print(f"rat 3: {rat3.attack} should equal 3.")

def test_for_rats():
    game = Game()
    rat = Rat(game, "rato1")
    rat2 = Rat(game, "rato2")
    rat3 = Rat(game, "rato3")
    rat4 = Rat(game, "rato4")

    print(f"rat 1: {rat.attack} should equal 4.")
    print(f"rat 2: {rat2.attack} should equal 4.")
    print(f"rat 3: {rat3.attack} should equal 4.")
    print(f"rat 4: {rat4.attack} should equal 4.")


test_single_rat()
print("\n")
test_two_rats()
print("\n")
test_three_rats()
print("\n")
test_for_rats()