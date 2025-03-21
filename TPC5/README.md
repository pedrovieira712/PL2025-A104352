# TPC5 - Máquina de Vending

## Identificação
- **Nome:** Pedro de Seabra Vieira  
- **Número:** A104352  
- **Data:** 13/03/2025  
- **Foto:**  
  ![Foto](../assets/img/FotoPerfil.png)

---

## Problema

O objetivo deste trabalho foi desenvolver um programa que simule o funcionamento de uma máquina de vending. A máquina deve gerir um stock de produtos, que é armazenado num ficheiro JSON (`stock.json`), e permitir ao utilizador interagir através de comandos para listar produtos, adicionar moedas, selecionar produtos e sair, recebendo o troco. O stock é carregado no início do programa e atualizado no ficheiro ao terminar, mantendo o estado entre execuções.

A máquina aceita os seguintes comandos:
- `LISTAR`: Mostra o stock atual de produtos.
- `MOEDA <valor>`: Adiciona moedas ao saldo (ex.: `MOEDA 1e, 20c, 5c`).
- `SELECIONAR <código>`: Seleciona um produto pelo código (ex.: `SELECIONAR A23`).
- `SAIR`: Termina o programa e devolve o troco.

O programa deve lidar com cenários como produtos inexistentes, stock esgotado e saldo insuficiente. Como extra, o enunciado sugere a implementação de um comando para adicionar produtos ao stock, mas este não foi implementado nesta versão.

---

## Explicação do Problema

O desafio consistiu em criar um simulador de uma máquina de vending que opera com base num stock de produtos armazenado num ficheiro JSON. Cada produto é representado por um dicionário com as chaves `cod` (código do produto, ex.: `A23`), `nome` (nome do produto), `quant` (quantidade disponível) e `preco` (preço em euros). O programa utiliza a biblioteca `ply.lex` para tokenizar os comandos inseridos pelo utilizador, permitindo processar entradas como `MOEDA 1e, 20c` ou `SELECIONAR A23`.

Os principais desafios foram:
- **Tokenização dos Comandos**: Usar `ply.lex` para reconhecer comandos (`LISTAR`, `MOEDA`, etc.), códigos de produtos (ex.: `A23`) e valores de moedas (ex.: `1e`, `20c`).
- **Gestão do Stock**: Carregar o stock de `stock.json` no início e gravá-lo ao sair, atualizando as quantidades após cada compra.
- **Gestão do Saldo**: Converter moedas inseridas (em euros e cêntimos) para cêntimos, verificar se o saldo é suficiente para comprar um produto e calcular o troco ao sair.
- **Tratamento de Erros**: Lidar com entradas inválidas (ex.: comandos sem argumentos, moedas não aceites) e cenários como produtos inexistentes ou stock esgotado.

A solução implementada tokeniza os comandos usando expressões regulares definidas com `ply.lex`. Os tokens incluem `COMMAND` (para comandos como `LISTAR`), `POSITION` (para códigos de produtos como `A23`), `MONEY` (para valores de moedas), `EUR` (euros) e `CENT` (cêntimos). O programa processa cada comando, executa a ação correspondente e fornece feedback ao utilizador.

Foram adicionadas verificações para entradas inválidas:
- Se o utilizador inserir uma entrada vazia, é mostrada a mensagem: `maq: Erro, os comandos possíveis são: LISTAR, MOEDA, SELECIONAR, SAIR.`.
- Se o comando `SELECIONAR` ou `MOEDA` for inserido sem argumentos, é mostrada uma mensagem indicando o formato correto (ex.: `maq: SELECIONAR <código> (ex.: SELECIONAR A23).`).

---

## Comandos

O programa suporta os seguintes comandos:

- **`LISTAR`**  
  Mostra o stock atual de produtos num formato tabular, incluindo o código, nome, quantidade e preço de cada produto.  
  **Exemplo:**
```
>> LISTAR
cod | nome | quantidade | preço
--- | ---- | ---------- | -----
A23 | água 0.5L | 6 | 0.70€
B45 | refrigerante 0.33L | 4 | 1.20€
C67 | chocolate preto 100g | 10 | 0.90€
D89 | sumo laranja 0.2L | 8 | 1.00€
E01 | barra de cereais | 12 | 0.50€
F34 | café expresso | 5 | 0.80€
G56 | sanduíche de frango | 3 | 2.50€
H78 | batatas fritas 50g | 7 | 1.30€
```

- **`MOEDA <valor>`**  
Adiciona moedas ao saldo do utilizador. As moedas devem ser especificadas no formato `1e` (euros) ou `20c` (cêntimos), separadas por vírgulas. Apenas moedas de 1, 2, 5, 10, 20, 50 cêntimos e 1, 2 euros são aceites.  
**Exemplo:**
```
>> MOEDA 1e, 20c
maq: Saldo = 1e20c
```

- **`SELECIONAR <código>`**  
Tenta comprar um produto com o código especificado (ex.: `A23`). Verifica se o produto existe, se há stock disponível e se o saldo é suficiente. Se a compra for bem-sucedida, a quantidade do produto é reduzida e o saldo é atualizado.  
**Exemplo:**
```
>> SELECIONAR A23
maq: Pode retirar o produto dispensado 'água 0.5L'
maq: Saldo = 0e50c
```

Outros cenários tratados:
- Produto inexistente: `maq: Produto com código 'X99' não encontrado.`
- Stock esgotado: `maq: Produto 'nome' está fora de stock.`
- Saldo insuficiente: `maq: Saldo insuficiente para 'nome'.`

- **`SAIR`**  
Termina o programa, devolvendo o troco (se houver saldo) e gravando o stock atualizado no ficheiro `stock.json`.  
**Exemplo:**
```
>> SAIR
maq: Pode retirar o troco: 1x 50c.
maq: Até à próxima.
```

---

## Conclusão

O programa implementado cumpre os requisitos principais do enunciado, simulando uma máquina de vending com gestão de stock, saldo e troco. A utilização do `ply.lex` permitiu uma tokenização robusta dos comandos, facilitando o processamento de entradas complexas como `MOEDA 1e, 20c`. Foram tratados cenários de erro, como entradas vazias, comandos sem argumentos, produtos inexistentes e saldo insuficiente, com mensagens informativas para o utilizador.

No entanto, o comando extra `ADICIONAR` (para adicionar produtos ao stock) não foi implementado nesta versão. Como melhoria futura, poderia ser adicionado suporte para este comando, bem como validações mais rigorosas para moedas (ex.: rejeitar valores negativos) e mensagens de erro mais detalhadas com rastreamento de linha/coluna.