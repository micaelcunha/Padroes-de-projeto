from pessoa import Pessoa


class OperadorEscala:
    def __init__(self, pessoa: Pessoa) -> None:
        self.pessoa = pessoa
        pessoa.eventos.append(self.embarcar)
        
    def embarcar(self, nome_atributo: str, value: int) -> None:
        if (nome_atributo == "idade"):
            if (value < 16):
                print("Não embarca.")
            else:
                print("Pode embarcar")
                self.pessoa.eventos.remove(
                    self.embarcar
                )