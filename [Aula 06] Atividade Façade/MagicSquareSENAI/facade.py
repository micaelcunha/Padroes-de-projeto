from generator import Generator
from splitter import Splitter
from verifier import Verifier


class MagicSquareGenerator:
    def generate(self, size: int):
        generator = Generator()
        splitter = Splitter()
        verifier = Verifier()
        
        while True:
            matriz = []
            for i in range(size):
                matriz.append(generator.generate(size))
            
            square = splitter.split(matriz)
            cubo_magico: bool = verifier.verify(square)

            # Código aqui...
            if cubo_magico:
                return matriz
            else:
                print(matriz)
