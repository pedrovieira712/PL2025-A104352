# TPC1 - Somador On/Off

## Identificação
- **Nome:** Pedro de Seabra Vieira
- **Número:** A104352
- **Data:** 13/02/2025
- **Foto:** 
  ![Foto](/assets/img/FotoPerfil.png)

## Problema
1. Some todas as sequências de dígitos que encontre num texto;  
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;  
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;  
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída;  
5. No fim, coloca o valor da soma na saída.

## Explicação do Problema
O programa processa uma sequência de carácteres, somando os números encontrados de forma condicional. A lógica de funcionamento é a seguinte:

- O programa percorre o texto carácter a carácter.
- Quando encontra um dígito, armazena-o para formar um número completo, ou seja, até encontrar um caractér não numérico.
- Se encontrar um "-" seguido de um dígito, interpreta-o como um número negativo.
- Quando encontra um carácter não numérico:
  - Se a soma estiver ativa, adiciona o número acumulado ao total.
  - Se for "On", ativa a soma.
  - Se for "Off", desativa a soma.
  - Se for "=", imprime o valor o valor atual.
- No final do texto, soma qualquer número restante e apresenta o resultado final.

   
## Exemplos de Uso

### Exemplo 1
- **Entrada:** `1a2b3c4d=oN5e6f7g=OfF8h9i=on10j11k`
- **Saída:** 
  ```
  10
  28
  28
  49
  ```

### Exemplo 2
- **Entrada:** `123#$%ON5678!!ofF-999-9=On1111=2222=`
- **Saída:**
  ```
  5801
  6912
  9134
  9134
  ```

## Resultados
O programa permite processamento flexível de texto, com capacidade de:
- Somar números em sequência
- Controlar o processo de soma dinamicamente
- Registrar resultados intermediários
- Lidar com diversos formatos de entrada

## Considerações Finais
- Não utiliza expressões regulares
- Processa entrada via input do usuário
- Envia resultados para stdout
