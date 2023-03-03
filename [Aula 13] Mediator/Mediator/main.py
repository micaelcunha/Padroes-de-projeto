from componente_1 import Componente1
from componente_2 import Componente2
from implementacao_mediator import ImplementacaoMediator


componente_1 = Componente1()
componente_2 = Componente2()
mediator = ImplementacaoMediator(componente_1, componente_2)
componente_1.fazer_A()

print("\n")
print("\n")

componente_2.fazer_D()