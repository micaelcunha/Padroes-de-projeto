from componente_1 import Componente1
from componente_2 import Componente2
from mediator import Mediator


class ImplementacaoMediator(Mediator):
    def __init__(self, componente_1: Componente1, componente_2: Componente2) -> None:
        self._componente_1 = componente_1
        self._componente_1.mediator = self
        self._componente_2 = componente_2
        self._componente_2.mediator = self
        
    def notificar(self, mensagem: str):
        if (mensagem == "A"):
            print("Chegou mensagem no mediador do componente_1 'A' pra fazer a seguinte operação: ")
            self._componente_2.fazer_C()
        if (mensagem == "D"):
            print("Chegou mensagem no mediador do componente_2 'D' pra fazer a seguinte operação: ")
            self._componente_1.fazer_B()
            self._componente_2.fazer_C()
        