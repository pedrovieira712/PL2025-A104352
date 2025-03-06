import ply.lex as lex
import sys
import os

# Definir os tokens
tokens = (
    "SELECT",          # Palavra-chave 'select'
    "WHERE",           # Palavra-chave 'where'
    "LIMIT",           # Palavra-chave 'limit'
    "ATTRIBUTE",       # Palavra-chave 'a' (abreviação de rdf:type)
    "URI",             # URIs como dbo:MusicalArtist
    "VARIABLE",        # Variáveis como ?nome, ?desc
    "LITERAL",         # Literais como "Chuck Berry"@en
    "NUMBER",          # Números como 1000
    "LBRACE",          # {
    "RBRACE",          # }
    "DOT",             # .
    "COMMENT",         # Comentários como # DBPedia: obras de Chuck Berry
)

# Regras de correspondência para os tokens
def t_SELECT(t):
    r'[Ss][Ee][Ll][Ee][Cc][Tt]'   
    return t

def t_WHERE(t):
    r'[Ww][Hh][Ee][Rr][Ee]'   
    return t

def t_LIMIT(t):
    r'[Ll][Ii][Mm][Ii][Tt]'   
    return t

def t_ATTRIBUTE(t):
    r'a'  
    return t

def t_URI(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*:[a-zA-Z_][a-zA-Z0-9_]*'  
    return t

def t_VARIABLE(t):
    r'\?[a-zA-Z_][a-zA-Z0-9_]*'  
    return t

def t_LITERAL(t):
    r'"[^"]*"(?:@[a-zA-Z]+)?'   
    return t

def t_NUMBER(t):
    r'\d+'   
    t.value = int(t.value)   
    return t

t_LBRACE = r'{'
t_RBRACE = r'}'
t_DOT = r'\.'

def t_COMMENT(t):
    r'\#.*?(?=\n|$)'  
    t.value = t.value.strip()  
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 analisador.py <caminho_do_arquivo>")
        sys.exit(1)

    input_filename = sys.argv[1]

    output_filename = os.path.join(os.path.dirname(input_filename), "output.txt")

    print(f"Arquivo {input_filename} processado > {output_filename}")
    try:
        with open(input_filename, "r") as file:
            with open(output_filename, "w") as output_file:
                for line in file:
                    lexer.input(line)
                    for token in lexer:
                        output_file.write(f"Token: {token.type}, Valor: {token.value}\n")
    except FileNotFoundError as e:
        print(f"Erro: Arquivo '{input_filename}' não encontrado. Detalhes: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()