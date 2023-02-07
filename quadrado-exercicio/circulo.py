class Circulo:
    def __init__(self, raio: int) -> None:
        self.raio = raio

    def calcular_area(self) -> float:
        resultado = 3.14 * (self.raio**2)
        return resultado