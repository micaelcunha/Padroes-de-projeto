from observer import Observer
from game import Game
from rat import Rat


def test_single_rat():
    game = Game()
    observer = Observer()
    rat = Rat(observer)
    print(f"rat 1: {rat.attack} should equal 1.")


def test_two_rats():
    game = Game()
    observer = Observer()
    rat = Rat(observer)
    rat2 = Rat(observer)

    print(f"rat 1: {rat.attack} should equal 2.")
    print(f"rat 2: {rat2.attack} should equal 2.")
    
    rat3 = Rat(observer)

    print(f"rat 3: {rat3.attack} should equal 3.")


test_single_rat()
print("\n")
test_two_rats()