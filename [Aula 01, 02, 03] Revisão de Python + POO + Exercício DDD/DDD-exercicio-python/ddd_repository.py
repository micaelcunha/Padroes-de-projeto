from ddd import DDD

class DddRepository():
    def __init__(self) -> None:
        self.ddd_repository: DDD = []
        
    def get(self, numero_ddd: int) -> str:
        for ddd in self.ddd_repository:
            if(numero_ddd == ddd.numero_ddd):
              return ddd.nome_cidade
        
    def append(self, ddd: DDD) -> None:
        self.ddd_repository.append(ddd)
        
    def check(self, numero_ddd: int) -> bool:
        for ddd in self.ddd_repository:
            if(ddd.numero_ddd == numero_ddd):
                return True
            
        return False