# TPC3 - Conversor de Markdown para HTML

## Identificação
- **Nome:** Pedro de Seabra Vieira  
- **Número:** A104352  
- **Data:** 28/02/2025
- **Foto:**  
  ![Foto](/assets/img/FotoPerfil.png)

---

## Problema
Criar em Python um pequeno conversor de Markdown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

### Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
**In:** `# Exemplo`  
**Out:** `<h1>Exemplo</h1>`

### Bold: pedaços de texto entre "**"
**In:** `Este é um **exemplo** ...`  
**Out:** `Este é um <b>exemplo</b> ...`

### Itálico: pedaços de texto entre "*"
**In:** `Este é um *exemplo* ...`  
**Out:** `Este é um <i>exemplo</i> ...`

### Lista numerada:
**In:**
```
1. Primeiro item
2. Segundo item
3. Terceiro item
```

**Out:** 
```
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```

### Link: [texto](endereço URL)

In: `Como pode ser consultado em [página da UC](http://www.uc.pt)`

Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`

### Imagem: ![texto alternativo](path para a imagem)

In: Como se vê na imagem seguinte: `![imagem dum coelho](http://www.coellho.com) ...`

Out: `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...`

---
## Explicação do Problema
O conversor foi implementado em Python utilizando expressões regulares (`re`) para identificar e transformar os elementos de Markdown em HTML. O código funciona da seguinte forma:
1. **Leitura do ficheiro Markdown:** O programa lê o conteúdo de um ficheiro `.md` fornecido como argumento na linha de comando.
2. **Processamento linha a linha:**
   - **Cabeçalhos:** Deteta `#` no início da linha e converte para `<h1>` até `<h6>` consoante o número de `#`.
   - **Listas numeradas:** Reconhece linhas começadas por números (ex.: `1.`) e agrupa-as numa tag `<ol>` com itens `<li>`.
   - **Negrito e itálico:** Usa `re.sub()` para substituir `**texto**` por `<b>texto</b>` e `*texto*` por `<i>texto</i>`.
   - **Links e imagens:** Substitui `[texto](URL)` por `<a href="URL">texto</a>` e `![alt](URL)` por `<img src="URL" alt="alt">`
3. **Escrita do HTML:** O resultado é gravado num ficheiro `.html` com o mesmo nome do ficheiro de entrada, mas com extensão alterada.
4. **Gestão de erros:** Inclui tratamento de exceções para ficheiros não encontrados.

O programa é executado via terminal com o comando `python3 script.py ficheiro.md`.
---

## Resultados
### Input
```
# Título Exemplo
Este é um texto com **negrito** e *itálico*.  
1. Item um  
2. Item dois  
Veja [este site](http://exemplo.com) e esta ![imagem](http://imagem.com).
```

### Output
```
<h1>Título Exemplo</h1>
Este é um texto com <b>negrito</b> e <i>itálico</i>.
<ol>
<li>Item um</li>
<li>Item dois</li>
</ol>
Veja <a href="http://exemplo.com">este site</a> e esta <img src="http://imagem.com" alt="imagem">.
```
 