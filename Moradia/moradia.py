from endereco import Endereco

class Moradia:
    def __init__(self) -> None:
        self.endereco = Endereco()

    def area(self) -> float:
        pass

    def endereco(self) -> Endereco:
        return self.endereco