from chat_room import *


class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.chat_log = []
        self.chat_room: ChatRoom = None

    def receive(self, sender: str, message: str) -> None:
        s = f"{sender}: {message}"
        print(f"[{self.name}\'s chat session] {s}")
        self.chat_log.append(s)

    def say(self, message: str) -> None:
        self.chat_room.broadcast(self.name, message)

    def private_message(self, who: str, message: str) -> None: 
        self.chat_room.message(self.name, who, message)
