import re
import sys

def markdown_para_html(texto):
    linhas = texto.split("\n")
    html = []
    dentro_ol = False   

    for linha in linhas:
        # Titulos  
        match = re.match(r'^(#{1,6})\s*(.*)', linha)
        if match:
            nivel = len(match.group(1))   
            conteudo = match.group(2)
            html.append(f"<h{nivel}>{conteudo}</h{nivel}>")
            continue

        # Listas numeradas  
        match = re.match(r'^\d+\.\s+(.*)', linha)
        if match:
            if not dentro_ol:
                html.append("<ol>")
                dentro_ol = True
            html.append(f"<li>{match.group(1)}</li>")
            continue
        else:
            if dentro_ol:
                html.append("</ol>")  
                dentro_ol = False

        # Negrito  
        linha = re.sub(r'\*{2}(.*?)\*{2}', r'<b>\1</b>', linha)

        # Itálico  
        linha = re.sub(r'\*(.*?)\*', r'<i>\1</i>', linha)

        # Imagem
        linha = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', linha)

        # Hiperligação
        linha = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', linha)

        html.append(linha)

    if dentro_ol:
        html.append("</ol>")

    return "\n".join(html)

def converter_ficheiro_markdown(entrada, saida):
    try:
        with open(entrada, "r", encoding="utf-8") as f:
            conteudo_markdown = f.read()
        
        conteudo_html = markdown_para_html(conteudo_markdown)

        with open(saida, "w", encoding="utf-8") as f:
            f.write(conteudo_html)
        
        print(f"HTML output: " + saida)

    except FileNotFoundError:
        print(f"Error: '{entrada}' not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("python3 script.py file.md")
    else:
        ficheiro_md = sys.argv[1]
        ficheiro_html = ficheiro_md.replace(".md", ".html")   
        converter_ficheiro_markdown(ficheiro_md, ficheiro_html)