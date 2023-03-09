from operador_escala import OperadorEscala
from pessoa import Pessoa


pessoa = Pessoa()
operador_escala = OperadorEscala(pessoa)
for idade in range(14, 20):
    print(f"Embarcando pessoa com idade de {idade}")
    pessoa.idade = idade
