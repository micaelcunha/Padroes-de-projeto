from generator import Generator
from splitter import Splitter
from verifier import Verifier


class MagicSquareGenerator:
    def generate(self, size: int):
        generator = Generator()
        splitter = Splitter()
        verifier = Verifier()

        while True:
            square = []
            for i in range(size):
                square.append(generator.generate(size))
            s = splitter.split(square)
            verifier.verify(s)

            # Código aqui...
        
            return square
