from event import Event


class Person:
    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)