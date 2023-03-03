from chat_room import ChatRoom
from person import Person

room = ChatRoom()

jefte = Person("Jefté")
brenno = Person("Brenno")
barbara = Person("Bárbara")

room.join(jefte)
room.join(brenno)
room.join(barbara)

jefte.say("Hi room!")
brenno.say("Oh, hey Jefté, how are you?")
brenno.say("Great.")
barbara.say("Hi guys.")

sabrina = Person("Sabrina")
room.join(sabrina)

sabrina.private_message("Jefté", "Meow ;P")