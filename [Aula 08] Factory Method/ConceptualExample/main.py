from concrete_creator_1 import ConcreteCreator1
from concrete_creator_2 import ConcreteCreator2
from creator import Creator


def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


print("App: Launched with the ConcreteCreator1.")
client_code(ConcreteCreator1())
print("\n")

print("App: Launched with the ConcreteCreator2.")
client_code(ConcreteCreator2())
