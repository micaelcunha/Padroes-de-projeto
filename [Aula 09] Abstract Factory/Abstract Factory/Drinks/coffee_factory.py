from coffee import Coffee
from hot_drink_factory import HotDrinkFactory


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount}ml enjoy!")
        return Coffee()
