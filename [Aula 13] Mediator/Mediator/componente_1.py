from componente_base import ComponenteBase


class Componente1(ComponenteBase):
    def fazer_A(self):
        print("Componente 1 fazendo alguma coisa de A")
        self.mediator.notificar("A")
        
    def fazer_B(self):
        print("Componente 1 fazendo alguma coisa de B")
        self.mediator.notificar("B")