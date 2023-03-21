from quadrado import Quadrado

class QuadradoParaCirculo:
    def __init__(self, quadrado: Quadrado) -> None:
        self.quadrado = quadrado

    def calcular_area(self) -> float:
        raio = self.quadrado.lado
        return 3.14 * (raio ** 2)