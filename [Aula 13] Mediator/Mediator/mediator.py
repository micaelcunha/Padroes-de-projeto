from abc import ABC


class Mediator(ABC):
    def notificar(self, mensagem: str):
        pass