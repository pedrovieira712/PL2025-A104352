# TPC2 - Análise de um dataset de obras musicais

## Identificação
- **Nome:** Pedro de Seabra Vieira
- **Número:** A104352
- **Data:** 17/02/2024
- **Foto:**  
  ![Foto](/assets/img/FotoPerfil.png)

## Problema
Este TPC consiste na leitura e análise de um dataset CSV onde contém informações sobre obras musicais. 

- **É proibido utilizar o módulo CSV do Python** para a leitura dos dados;
- O dataset deve ser processado manualmente, tratando cada linha e separando os valores de acordo com o delimitador `";"`;
- O programa deve produzir os seguintes resultados:
  1. Uma lista ordenada alfabeticamente de todos os **compositores** presentes no dataset;
  2. A **distribuição das obras por período**, ou seja, quantas obras pertencem a cada período musical;
  3. Um **dicionário** em que cada período está associado a uma lista ordenada alfabeticamente dos títulos das obras pertencentes a esse período.

## Explicação do Problema
O problema consiste na manipulação de um **ficheiro CSV** sem recorrer a bibliotecas especializadas, realizando a leitura dos dados **linha a linha**, extraindo as colunas relevantes e processando as informações conforme os requisitos.   

A resolução do problema envolve as seguintes etapas:
1. **Leitura do ficheiro**: O programa abre o ficheiro e extrai os dados manualmente.
2. **Processamento dos dados**:
   - Criar uma lista única e ordenada dos compositores.
   - Contar quantas obras existem em cada período.
   - Agrupar os títulos das obras por período e ordená-los alfabeticamente.
3. **Apresentação dos resultados** de forma estruturada no terminal.

## Resultados

### Output com o ficheiro CSV fornecido pela equipa docente
Abaixo apresenta-se um exemplo de saída gerada ao executar o programa com o ficheiro `obras.csv` fornecido pelos docentes:

```
-> Compositores
Bach, Johann Michael
Boyvin, Jacques
Bull, John
Estevao de Brito
John IV
Manuel Cardoso
Manuel Rodriguez Coelho

-> Distribuição por Período
Renascimento: 1 obras
Medieval: 4 obras
Contemporâneo: 1 obras
Século XX: 1 obras

-> Títulos por Período

Renascimento:
  - Estampes

Medieval:
  - Impromptu, Op. 29
  - Mazurkas, Op. 30
  - Serenade for Strings
  - clarinet and piano

Contemporâneo:
  - Impromptu, Op. 36

Século XX:
  - poems
```