from person import Person


class ChatRoom:
    def __init__(self) -> None:
        self.peoples: list[Person] = []

    def join(self, person: Person):
        self.broadcast("room",  f"{person.name} joins the chat")
        person.chat_room = self
        self.peoples.append(person)

    def broadcast(self, source: str, message: str) -> None:
        for person in self.peoples:
            if person.name != source:
                person.receive(source, message)

    def message(self, source, destination: str, message: str) -> None:
        for person in self.peoples:
            if person.name == destination:
                person.receive(source, message)