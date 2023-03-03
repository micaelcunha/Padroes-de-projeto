from sub_sistema_1 import SubSistema1
from sub_sistema_2 import SubSistema2

class Facade:
    def __init__(self, sub_sistema_1: SubSistema1, sub_sistema_2: SubSistema2) -> None:
        self.sub_sistema_1 = sub_sistema_1
        self.sub_sistema_2 = sub_sistema_2
        
    def operacoes(self) -> str:
        results: list = []
        results.append("Inicializando subsistema")
        results.append(self.sub_sistema_1.operacao_1())
        results.append(self.sub_sistema_2.operacao_2())
        
        results.append("Inicializando subsistema")
        results.append(self.sub_sistema_1.operacao_n())
        results.append(self.sub_sistema_2.operacao_z())
        
        return "\n".join(results)