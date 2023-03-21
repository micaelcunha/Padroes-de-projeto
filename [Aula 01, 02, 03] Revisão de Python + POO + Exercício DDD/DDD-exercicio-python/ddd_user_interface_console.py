from ddd_user_interface import UserInterface

class UserInterfaceConsole():
    def __init__(self, user_interface: UserInterface) -> None:
        self.user_interface = user_interface
        
    def input_user_ddd(self) -> str:   
        numero_ddd = input("Digite o DDD → ")
        
        resultado = self.user_interface.encontrar(int(numero_ddd))
        
        return resultado