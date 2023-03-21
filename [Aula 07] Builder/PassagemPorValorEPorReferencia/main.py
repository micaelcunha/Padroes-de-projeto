from pessoa import Pessoa


def incrementa(numero: int) -> None:
    numero += 10
    print(f"incrementa: {numero}")
    
def deixar_mais_velho(pessoa: Pessoa) -> None:
    pessoa.idade += 10
    
print("\n----------------------\n")
primeiro_numero = 10
print(f"1: {primeiro_numero}")
incrementa(primeiro_numero)
print(f"2: {primeiro_numero}")
print("\n----------------------\n")
pessoa = Pessoa("Samara", 8)
print(f"3: {pessoa.idade}")
deixar_mais_velho(pessoa)
print(f"4: {pessoa.idade}")

print("\n----------------------\n")