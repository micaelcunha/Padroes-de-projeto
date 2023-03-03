from componente_base import ComponenteBase


class Componente2(ComponenteBase):
    def fazer_C(self):
        print("Componente 2 fazendo alguma coisa de C")
        self.mediator.notificar("C")
        
    def fazer_D(self):
        print("Componente 2 fazendo alguma coisa de D")
        self.mediator.notificar("D")