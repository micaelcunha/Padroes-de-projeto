from quadrado import Quadrado
from circulo import Circulo
from quadrado_para_circulo import QuadradoParaCirculo


quadrado = Quadrado(10)
circulo = Circulo(3)
qpc = QuadradoParaCirculo()
print(f"Resultado do calculo do Quadrado: {qpc.calcular_area(quadrado)}")