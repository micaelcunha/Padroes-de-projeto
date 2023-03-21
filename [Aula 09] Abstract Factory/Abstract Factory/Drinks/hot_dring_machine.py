from available_drink import AvailableDrink
from coffee_factory import CoffeeFactory
from tea_factory import TeaFactory


class HotDrinkMachine:

    factories = []
    initialized = False

    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for available_drink in AvailableDrink:
                name = available_drink.name[0] + available_drink.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Available drinks:")
        for factory in self.factories:
            print(factory[0])

        s = input(f"Please pick drink (0-{len(self.factories)-1}): ")
        index = int(s)
        s = input(f"Specify amount: ")
        amount = int(s)
        return self.factories[index][1].prepare(amount)
