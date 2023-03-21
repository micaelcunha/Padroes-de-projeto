# Codificação de fachada

- Um quadrado mágico é uma matriz quadrada cujas linhas, colunas e diagonais somam o mesmo valor.
- Eu construí um sistema que nos ajuda a construir quadrados mágicos, mas é um pouco complicado. Atualmente é composto por três turmas:
   - **Generator** cria uma matriz de dígitos aleatórios (adequadamente restritos) de um comprimento específico.
     - Você pode usar este gerador várias vezes para construir uma matriz quadrada do tamanho necessário.
   - **Splitter** divide uma matriz quadrada 2D em várias listas contendo todas as linhas, todas as colunas e todas as diagonais.
   - **Verifier** garante que, dada uma lista de listas, todas as listas somam o mesmo valor.
- Usando todos os itens acima, implemente uma fachada MagicSquareGenerator que use todos esses três componentes para gerar um quadrado mágico válido do tamanho necessário.