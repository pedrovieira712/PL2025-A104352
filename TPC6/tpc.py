import ply.lex as lex

class Exp:
    def __init__(self, type, exp1, op, exp2):
        self.type = type
        self.exp1 = exp1
        self.op = op
        self.exp2 = exp2

    def calc(self):
        if self.op == '+':
            return self.exp1.calc() + self.exp2.calc()
        elif self.op == '-':
            return self.exp1.calc() - self.exp2.calc()
        elif self.op == '*':
            return self.exp1.calc() * self.exp2.calc()
        elif self.op == '/':
            return self.exp1.calc() / self.exp2.calc()

class Num:
    def __init__(self, value):
        self.value = value

    def calc(self):
        return self.value

tokens = ('MULT', 'DIV', 'PLUS', 'MINUS', "NUM", "LPAREN", "RPAREN")

t_NUM = r'\d+'   
t_MULT = r'\*'
t_DIV = r'\/'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t '

def t_error(t):
    print('Carácter desconhecido: ', t.value[0], 'Linha: ', t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex()

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb and prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)
        prox_simb = ('erro', '', 0, 0)

def rec_Unario():
    global prox_simb
    if prox_simb and prox_simb.type == 'PLUS':
        rec_term('PLUS')
        return 1   
    elif prox_simb and prox_simb.type == 'MINUS':
        rec_term('MINUS')
        return -1   
    return 1   

def rec_Num():
    global prox_simb
    if prox_simb and prox_simb.type == 'NUM':
        num = int(prox_simb.value)
        rec_term('NUM')
        return Num(num)
    else:
        parserError(prox_simb)
        return None

def rec_Fator():
    global prox_simb
    if prox_simb is None:
        parserError("Fim inesperado da expressão")
        return None

    if prox_simb.type == 'LPAREN':
        rec_term('LPAREN')
        expr = rec_Expr()
        if prox_simb and prox_simb.type == 'RPAREN':
            rec_term('RPAREN')
            return expr
        else:
            parserError(prox_simb)
            return None
    elif prox_simb.type in ('NUM', 'PLUS', 'MINUS'):
        sinal = rec_Unario()
        num = rec_Num()
        if num is None:
            return None
        return Num(sinal * num.calc())
    else:
        parserError(prox_simb)
        return None

def rec_Termo():
    global prox_simb
    res = rec_Fator()
    if res is None:
        return None
    while prox_simb and prox_simb.type in ('MULT', 'DIV'):
        if prox_simb.type == 'MULT':
            rec_term('MULT')
            fator = rec_Fator()
            if fator is None:
                return None
            res = Exp('MULT', res, '*', fator)
        elif prox_simb.type == 'DIV':
            rec_term('DIV')
            fator = rec_Fator()
            if fator is None:
                return None
            res = Exp('DIV', res, '/', fator)
    return res

def rec_Expr():
    global prox_simb
    res = rec_Termo()
    if res is None:
        return None
    while prox_simb and prox_simb.type in ('PLUS', 'MINUS'):
        if prox_simb.type == 'PLUS':
            rec_term('PLUS')
            termo = rec_Termo()
            if termo is None:
                return None
            res = Exp('PLUS', res, '+', termo)
        elif prox_simb.type == 'MINUS':
            rec_term('MINUS')
            termo = rec_Termo()
            if termo is None:
                return None
            res = Exp('MINUS', res, '-', termo)
    return res

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    return rec_Expr()

def main():
    print("Calculadora de Expressões Aritméticas (TPC6)")
    print("Insira uma expressão aritmética (ex.: 2+3, (9-2)*(13-4)) ou 'sair' para terminar.")
    
    while True:
        expr = input(">> ").strip()
        if expr.lower() == 'sair':
            print("Até à próxima!")
            break
        if not expr:
            print("Erro: insira uma expressão válida.")
            continue
        
        try:
            exp = rec_Parser(expr)
            if exp is None:
                print("Erro: não foi possível processar a expressão.")
                continue
            resultado = exp.calc()
            resultado_formatado = round(float(resultado), 1)
            print(f"Valor da Expressão: {resultado_formatado:.1f}!")
        except Exception as e:
            print(f"Erro ao processar a expressão: {e}")

if __name__ == "__main__":
    main()