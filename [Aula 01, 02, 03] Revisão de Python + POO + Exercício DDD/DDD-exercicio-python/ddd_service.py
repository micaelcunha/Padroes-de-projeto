from ddd import DDD
from ddd_repository import DddRepository

class DddService():
    def __init__(self, ddd_repository: DddRepository) -> None:
        self.ddd_repository = ddd_repository
        
        
    def encontrarCidade(self, numero_ddd: int) -> str:
        if(self.ddd_repository.check(numero_ddd)):
           return self.ddd_repository.get(numero_ddd)
       
        return "None"