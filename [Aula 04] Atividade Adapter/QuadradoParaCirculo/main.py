from quadrado import Quadrado
from quadrado_para_circulo import QuadradoParaCirculo

def calcular_area(forma):
    qpc = QuadradoParaCirculo(forma)
    return qpc.calcular_area()

quadrado = Quadrado(10)
print(f"Resultado do calculo do Quadrado: {calcular_area(quadrado)}")