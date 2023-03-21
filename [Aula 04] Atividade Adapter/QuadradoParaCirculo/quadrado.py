class Quadrado:
    def __init__(self, lado: int) -> None:
        self.lado = lado
        
    def calcular_area(self) -> int:
        return self.lado ** 2
