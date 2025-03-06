# TPC4 - Analisador Léxico

## Identificação
- **Nome:** Pedro de Seabra Vieira  
- **Número:** A104352  
- **Data:** 06/03/2025  
- **Foto:**  
  ![Foto](../assets/img/FotoPerfil.png)

---

## Problema
Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:

```
# DBPedia: obras de Chuck Berry 
 
select ?nome ?desc where { 
    ?s a dbo:MusicalArtist. 
    ?s foaf:name "Chuck Berry"@en . 
    ?w dbo:artist ?s. 
    ?w foaf:name ?nome. 
    ?w dbo:abstract ?desc 
} LIMIT 1000
```

---
## Explicação do Problema
O objetivo deste trabalho foi desenvolver um analisador léxico para uma linguagem de consulta baseada em SPARQL, utilizando a query fornecida como exemplo. Um analisador léxico tem a função de dividir o texto de entrada em unidades léxicas (tokens) significativas, ignorando elementos como espaços em branco e, opcionalmente, comentários, dependendo do comportamento desejado. A query fornecida contém diversos tipos de tokens, incluindo:

- **Comentários**: `# DBPedia: obras de Chuck Berry` (anotações que podem ser ignoradas ou tokenizadas).
- **Palavras-chave**: `select`, `where`, `LIMIT`, `a` (com `a` sendo uma abreviação para `rdf:type`).
- **Variáveis**: `?nome`, `?desc`, `?s`, `?w` (identificadas por prefixo `?`).
- **URIs**: `dbo:MusicalArtist`, `foaf:name`, `dbo:artist`, `dbo:abstract` (identificadores com prefixos).
- **Literais**: `"Chuck Berry"@en` (strings com anotações de idioma).
- **Números**: `1000` (valores numéricos).
- **Pontuação**: `{`, `}`, `.` (símbolos de estrutura).

O desafio incluía:
- Tokenizar corretamente todos esses elementos.
- Lidar com a insensibilidade a maiúsculas/minúsculas em palavras-chave (ex.: `LIMIT` ou `limit`).
- Receber o ficheiro de entrada como argumento de linha de comando (ex.: `python3 analisador.py ./results/input.txt`).
- Produzir uma saída em um ficheiro de texto (`output.txt`) com os tokens identificados.
A solução foi implementada usando a biblioteca `ply.lex`, que facilita a criação de analisadores léxicos em Python, com regras definidas para cada tipo de token. Inicialmente, os comentários eram ignorados (padrão em SPARQL), mas, para atender a uma possível expectativa pedagógica de exibir todos os elementos da entrada, o código foi ajustado para tokenizar os comentários como `COMMENT`.
---

## Resultados
### Input
```
# DBPedia: obras de Chuck Berry 
 
select ?nome ?desc where { 
    ?s a dbo:MusicalArtist. 
    ?s foaf:name "Chuck Berry"@en . 
    ?w dbo:artist ?s. 
    ?w foaf:name ?nome. 
    ?w dbo:abstract ?desc 
} LIMIT 1000
```

### Output
```
Token: COMMENT, Valor: # DBPedia: obras de Chuck Berry
Token: SELECT, Valor: select
Token: VARIABLE, Valor: ?nome
Token: VARIABLE, Valor: ?desc
Token: WHERE, Valor: where
Token: LBRACE, Valor: {
Token: VARIABLE, Valor: ?s
Token: ATTRIBUTE, Valor: a
Token: URI, Valor: dbo:MusicalArtist
Token: DOT, Valor: .
Token: VARIABLE, Valor: ?s
Token: URI, Valor: foaf:name
Token: LITERAL, Valor: "Chuck Berry"@en
Token: DOT, Valor: .
Token: VARIABLE, Valor: ?w
Token: URI, Valor: dbo:artist
Token: VARIABLE, Valor: ?s
Token: DOT, Valor: .
Token: VARIABLE, Valor: ?w
Token: URI, Valor: foaf:name
Token: VARIABLE, Valor: ?nome
Token: DOT, Valor: .
Token: VARIABLE, Valor: ?w
Token: URI, Valor: dbo:abstract
Token: VARIABLE, Valor: ?desc
Token: RBRACE, Valor: }
Token: LIMIT, Valor: LIMIT
Token: NUMBER, Valor: 1000

```
 