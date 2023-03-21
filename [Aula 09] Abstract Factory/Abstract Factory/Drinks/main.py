from coffee_factory import CoffeeFactory
from hot_dring_machine import HotDrinkMachine
from tea_factory import TeaFactory

# def make_drink(type):
#     if type == "tea":
#         return TeaFactory().prepare(200)
#     elif type == "coffee":
#         return CoffeeFactory().prepare(50)
#     else:
#         return None

# entry = input("What king of drink would you like? ")
# drink = make_drink(entry)

hot_drink_machine = HotDrinkMachine()
hot_drink_machine.make_drink()