from ddd_service import DddService

class UserInterface():
    def __init__(self, ddd_service: DddService) -> None:
        self.ddd_service = ddd_service
        
    def encontrar(self, numero_ddd: int) -> str:
        nome_cidade = self.ddd_service.encontrarCidade(numero_ddd)
        
        if nome_cidade == "None":
            return "DDD não encontrado"

        return f"O DDD informado é da cidade: {self.ddd_service.encontrarCidade(numero_ddd)}"