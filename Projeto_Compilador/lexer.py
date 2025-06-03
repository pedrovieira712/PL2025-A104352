import ply.lex as lex

tokens = (
    # Palavras reservadas
    'PROGRAM', 'BEGIN', 'END', 'VAR', 'INTEGER', 'REAL', 'BOOLEAN', 'STRING',
    'ARRAY', 'OF', 'IF', 'THEN', 'ELSE', 'WHILE', 'DO', 'FOR', 'TO', 'DOWNTO',
    'FUNCTION', 'PROCEDURE', 'CONST', 'TYPE', 'DIV', 'MOD', 'AND',
    'OR', 'NOT', 'TRUE', 'FALSE', 'READLN', 'WRITELN', 'READ', 'WRITE',
    'LENGTH',
    
    # Identificadores e literais
    'ID', 'INTEGER_CONST', 'REAL_CONST', 'STRING_CONST',
    
    # Operadores
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN', 'EQ', 'NEQ', 'LT', 'GT', 'LTE', 'GTE',
    
    # Delimitadores
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'COMMA', 'SEMICOLON', 'COLON', 'DOT', 'DOTDOT'
)

# ===== PALAVRAS RESERVADAS - Definidas com ER explícitas para case-insensitive =====

def t_PROGRAM(t):
    r'[pP][rR][oO][gG][rR][aA][mM]\b'
    return t

def t_PROCEDURE(t):
    r'[pP][rR][oO][cC][eE][dD][uU][rR][eE]\b'
    return t

def t_FUNCTION(t):
    r'[fF][uU][nN][cC][tT][iI][oO][nN]\b'
    return t

def t_BEGIN(t):
    r'[bB][eE][gG][iI][nN]\b'
    return t

def t_END(t):
    r'[eE][nN][dD]\b'
    return t

def t_CONST(t):
    r'[cC][oO][nN][sS][tT]\b'
    return t

def t_TYPE(t):
    r'[tT][yY][pP][eE]\b'
    return t

def t_VAR(t):
    r'[vV][aA][rR]\b'
    return t

def t_INTEGER(t):
    r'[iI][nN][tT][eE][gG][eE][rR]\b'
    return t

def t_REAL(t):
    r'[rR][eE][aA][lL]\b'
    return t

def t_BOOLEAN(t):
    r'[bB][oO][oO][lL][eE][aA][nN]\b'
    return t

def t_STRING(t):
    r'[sS][tT][rR][iI][nN][gG]\b'
    return t

def t_ARRAY(t):
    r'[aA][rR][rR][aA][yY]\b'
    return t

def t_OF(t):
    r'[oO][fF]\b'
    return t

def t_IF(t):
    r'[iI][fF]\b'
    return t

def t_THEN(t):
    r'[tT][hH][eE][nN]\b'
    return t

def t_ELSE(t):
    r'[eE][lL][sS][eE]\b'
    return t

def t_WHILE(t):
    r'[wW][hH][iI][lL][eE]\b'
    return t

def t_DOWNTO(t):
    r'[dD][oO][wW][nN][tT][oO]\b'
    return t

def t_DO(t):
    r'[dD][oO]\b'
    return t

def t_FOR(t):
    r'[fF][oO][rR]\b'
    return t

def t_TO(t):
    r'[tT][oO]\b'
    return t

def t_DIV(t):
    r'[dD][iI][vV]\b'
    return t

def t_MOD(t):
    r'[mM][oO][dD]\b'
    return t

def t_AND(t):
    r'[aA][nN][dD]\b'
    return t

def t_OR(t):
    r'[oO][rR]\b'
    return t

def t_NOT(t):
    r'[nN][oO][tT]\b'
    return t

def t_TRUE(t):
    r'[tT][rR][uU][eE]\b'
    return t

def t_FALSE(t):
    r'[fF][aA][lL][sS][eE]\b'
    return t

def t_READLN(t):
    r'[rR][eE][aA][dD][lL][nN]\b'
    return t

def t_WRITELN(t):
    r'[wW][rR][iI][tT][eE][lL][nN]\b'
    return t

def t_READ(t):
    r'[rR][eE][aA][dD]\b'
    return t

def t_WRITE(t):
    r'[wW][rR][iI][tT][eE]\b'
    return t

def t_LENGTH(t):
    r'[lL][eE][nN][gG][tT][hH]\b'
    return t

# ===== IDENTIFICADORES - DEVE vir DEPOIS das palavras reservadas =====
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    return t

# ===== OPERADORES E DELIMITADORES =====

# Operadores de dois caracteres devem vir antes dos de um caractere
t_ASSIGN = r':='
t_NEQ = r'<>'
t_LTE = r'<='
t_GTE = r'>='
t_DOTDOT = r'\.\.'

# Operadores simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQ = r'='
t_LT = r'<'
t_GT = r'>'

# Delimitadores
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_DOT = r'\.'

# ===== LITERAIS =====

# Números reais (deve vir antes de inteiros)
def t_REAL_CONST(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Números inteiros
def t_INTEGER_CONST(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Strings
def t_STRING_CONST(t):
    r'\'([^\']|\'\')*\''
    raw_value = t.value[1:-1]  # Remove aspas externas
    processed_value = raw_value.replace("''", "'")
    t.value = processed_value
    return t

# ===== COMENTÁRIOS =====

# Comentários de chaves { ... }
def t_COMMENT_BRACE(t):
    r'\{[^}]*\}'
    t.lexer.lineno += t.value.count('\n')
    pass  # Ignora o comentário

# Comentários de parênteses (* ... *)
def t_COMMENT_PAREN(t):
    r'$$\*(.|\n)*?\*$$'
    t.lexer.lineno += t.value.count('\n')
    pass  # Ignora o comentário

# ===== CONTROLO DE LINHAS E ESPAÇOS =====

# Ignorar espaços em branco e tabs
t_ignore = ' \t'

# Quebras de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ===== TRATAMENTO DE ERROS =====

def t_error(t):
    print(f"Erro léxico: Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# ===== CONSTRUÇÃO DO LEXER =====

# Construir o lexer
lexer = lex.lex()

# Função para testar o lexer
def test_lexer(data):
    lexer.input(data)
    tokens_list = []
    for tok in lexer:
        tokens_list.append((tok.type, tok.value, tok.lineno))
    return tokens_list
