from hot_drink_factory import HotDrinkFactory
from tea import Tea


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in tea bag, boil water, pour {amount}ml, enjoy!")
        return Tea()
