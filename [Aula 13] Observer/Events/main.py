from person import Person


def call_doctor(name: str, address: str):
    print(f"{name} needs a doct at {address}")

def custom_doctor(name: str, address: str):
    print(f"{name} ill")

person = Person("Dona Flor", "Pelourinho, Salvador, Bahia")
person.falls_ill.append(custom_doctor)
person.falls_ill.append(call_doctor)
print("\n")
print("First call:")
person.catch_a_cold()

print("\n")

person.falls_ill.remove(call_doctor)
print("Second call:")
person.catch_a_cold()