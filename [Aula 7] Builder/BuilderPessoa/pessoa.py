class Pessoa:
    def __init__(self) -> None:
        # Informações Básicas
        self.nome = None
        self.telefone = None
        self.endereco = None
        self.cep = None
        # Informações
        self.trabalho = None
        self.cargo = None
        self.salario = None
        
    def __str__(self) -> str:
        return f"Nome: {self.nome}, Endereço: {self.endereco}, Cep: {self.cep}, Telefone: {self.telefone}, Trabalho: {self.trabalho}, Cargo:{self.cargo}, Salário: {self.salario}"
        