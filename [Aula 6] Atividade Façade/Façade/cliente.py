from facade import Facade


class Cliente:
    def __init__(self, facade: Facade) -> None:
        self.facade = facade
    
    def executar_operacoes(self) -> None:
        print(self.facade.operacoes())