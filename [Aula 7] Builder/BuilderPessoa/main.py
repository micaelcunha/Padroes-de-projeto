from pessoa_builder import PessoaBuilder

pessoa_builder = PessoaBuilder()
pessoa = pessoa_builder.definir_informacoes_basicas.com_nome("Carla").com_cep("44007-222").com_telefone("(75) 9998999").mora_em("Feira de Santana").definir_informacoes_profissionais.com_cargo("Estagiária").com_salario("700,00").trabalha_em("SENAI")

print(pessoa_builder.build())

