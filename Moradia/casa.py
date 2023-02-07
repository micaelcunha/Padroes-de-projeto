from telhado import Telhado
from parede import Parede
from espelho import Espelho

class Casa:
    def __init__(self) -> None:
        self.telhado_externo = Telhado()
        self.telhado_interno = Telhado()
        self.parede_quarto = Parede()
        self.parede_banheiro = Parede()
        self.parede_cozinha = Parede()
        self.lista_espelho: Espelho = Espelho()

    def telhado_area_externa(self) -> Telhado:
        return self.telhado_externo

    def telhado_area_interna(self) -> Telhado:
        return self.telhado_interno

    def parede_quarto(self) -> Parede:
        return self.parede_quarto

    def parede_banheiro(self) -> Parede:
        return self.parede_banheiro

    def parede_cozinha(self) -> Parede:
        return self.parede_cozinha

    def espelho_corredor(self) -> Espelho:
        return self.lista_espelho
