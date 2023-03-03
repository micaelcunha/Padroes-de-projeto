from person import Person


class ChatRoom:
    def __init__(self) -> None:
        self.peoples: list[Person] = []

    def join(self, person: Person):
        self.peoples.append(person)
        self.broadcast(person.name,  f"{person.name} joins the chat")

    def broadcast(self, source: str, message: str) -> None:
        for person in self.peoples:
            if person.name == source:
                person.receive("room", message)

    def message(self, source, destination: str, message: str) -> None:
        pass