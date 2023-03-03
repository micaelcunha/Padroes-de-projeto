from pessoa import Pessoa


class PessoaBuilder:
    def __init__(self, pessoa: Pessoa = None) -> None:
        if (pessoa is None):
            self.pessoa = Pessoa()
        else:
            self.pessoa = pessoa
    
    @property
    def definir_informacoes_basicas(self):
        return PessoaInformacoesBasicasBuilder(self.pessoa)
    
    @property
    def definir_informacoes_profissionais(self):
        return PessoaProfissionalBuilder(self.pessoa)

    def build(self) -> Pessoa:
        return self.pessoa

class PessoaInformacoesBasicasBuilder(PessoaBuilder):
    def __init__(self, pessoa: Pessoa = None) -> None:
        super().__init__(pessoa)
    
    def com_nome(self, nome: str):
        self.pessoa.nome = nome
        return self
        
    def mora_em(self, endereco: str):
        self.pessoa.endereco = endereco
        return self
        
    def com_cep(self, cep: str):
        self.pessoa.cep = cep
        return self
        
    def com_telefone(self, telefone: str):
        self.pessoa.telefone = telefone
        return self
        
class PessoaProfissionalBuilder(PessoaBuilder):
    def __init__(self, pessoa: Pessoa = None) -> None:
        super().__init__(pessoa)
    
    def trabalha_em(self, trabalho: str):
        self.pessoa.trabalho = trabalho
        return self
        
    def com_cargo(self, cargo: str):
        self.pessoa.cargo = cargo
        return self
        
    def com_salario(self, salario: str):
        self.pessoa.salario = salario
        return self