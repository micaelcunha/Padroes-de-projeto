from ddd import DDD
from ddd_repository import DddRepository
from ddd_service import DddService
from ddd_user_interface import UserInterface
from ddd_user_interface_console import UserInterfaceConsole


ddd_repository = DddRepository()

ddd_repository.append(DDD(11, "São Paulo"))
ddd_repository.append(DDD(75, "Feira de Santana"))
ddd_repository.append(DDD(71, "Salvador"))

ddd_service = DddService(ddd_repository)
user_interface = UserInterface(ddd_service)
user_interface_console = UserInterfaceConsole(user_interface)

while True:
    
    result = user_interface_console.input_user_ddd()
    if result == "DDD não encontrado":
        print(result)
        break
    else:
         print(result)