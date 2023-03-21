from cliente import Cliente
from facade import Facade
from sub_sistema_1 import SubSistema1
from sub_sistema_2 import SubSistema2


subsystem1 = SubSistema1()
subsystem2 = SubSistema2()
facade = Facade(subsystem1, subsystem2)
cliente = Cliente(facade)
cliente.executar_operacoes()