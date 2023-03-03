- [1. Clean code](#1-clean-code)
  - [1.1. Nomes de variáveis ruins](#11-nomes-de-variáveis-ruins)
    - [1.1.1. Nomes misteriosos](#111-nomes-misteriosos)
    - [1.1.2. Nomes exagerados](#112-nomes-exagerados)
    - [1.1.3. Nomes com tipo da variável](#113-nomes-com-tipo-da-variável)
    - [1.1.4. Nome ambigous](#114-nome-ambigous)
    - [1.1.5. Nomes redundantes](#115-nomes-redundantes)
    - [1.1.6. Resumo](#116-resumo)
  - [1.2. Convenção](#12-convenção)
  - [1.3. Assinatura dos métodos](#13-assinatura-dos-métodos)
  - [Muitos parâmetros dentro do método](#muitos-parâmetros-dentro-do-método)
  - [Parametros no topo](#parametros-no-topo)
  - [Parametros de saida](#parametros-de-saida)
  - [Numeros magicos](#numeros-magicos)


# 1. Clean code

## 1.1. Nomes de variáveis ruins

### 1.1.1. Nomes misteriosos

- Não devemos usar nomes misteriosos, pois gasta energia
- Nomes ruins:
  - dr1: SqlDataReader
  - page1: Page
  - od: int

### 1.1.2. Nomes exagerados

### 1.1.3. Nomes com tipo da variável

- Evitar no código
  - intIdade
  - strNome
  - array_Produtos
- Mas faz sentido no front, para identificar o tipo do elemento visual.

### 1.1.4. Nome ambigous

- Evitar nomes que dizem mais de uma coisa
  - nomeDoIncidenteID: int
  - multiSelect: bool

### 1.1.5. Nomes redundantes

  - oCliente: Cliente
  - listaDeClientesElegives: list[Cliente]

### 1.1.6. Resumo

- Nomes não tão curtos nem tão grandes
- Revelar a inteção da variável
- O nome da variável deve estar relacionado ao domínio

## 1.2. Convenção

- Toda linguagem tem sua própria convenção, ou seja a comunidade criou um **style code** para um bom entendimento entre os programadores da comunidade.
- Se atenta para a forma como escrevemos as variáveis, arquivos, classes:
- Snake case: snake_case
- Pascal case: PascalCase
- Camel case: camelCase

## 1.3. Assinatura dos métodos

- Evitar:
  - def buscar_cliente(id_incidente: str) -> Fruta:
- [Código de Exemplo](AssinaturaRuim/)

## Muitos parâmetros dentro do método

- Evitar colocar muitos pâmetros, no máximo 4, passando disso criar uam class para encapsular os parametros.

## Parametros no topo

- Evitar que todas as variaveis fiquem no topo, sempre que possivel.

## Parametros de saida

- Sempre que possóvel encapsular muitos retornos dentro de uma entidade (classe)

## Numeros magicos

- Evitar
  - Status == "A"
  - Status == 1