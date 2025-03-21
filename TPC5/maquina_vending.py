import ply.lex as lex
import json

moedas_aceites = [1, 2, 5, 10, 20, 50, 100, 200]

reserved = {
    "listar": "LISTAR",
    "moeda": "MOEDA",
    "selecionar": "SELECIONAR",
    "sair": "SAIR",
}

tokens = [
    "COMMAND",
    "MONEY",
    "EUR",
    "CENT",
    "POSITION"
] + list(reserved.values())

t_POSITION = r'[A-Z]\d+'

def t_MONEY(t):
    r'\d+[e|c]'
    if converter_saldo_para_cents(t.value) not in moedas_aceites:
        raise ValueError(f"Moeda não aceite: {t.value}")
    if "e" in t.value:
        t.type = "EUR"
    elif "c" in t.value:
        t.type = "CENT"
    return t

def t_COMMAND(t):
    r'\b[a-z|A-Z]+\b'
    t.type = reserved.get(t.value.lower(), "COMMAND")
    return t

t_ignore = ' ,.'

def t_error(t):
    raise ValueError(f"Valor inválido: {t.value}")

def listar(stock):
    print("cod | nome | quantidade | preço")
    print("--- | ---- | ---------- | -----")

    for produto in stock:
        cod = produto["cod"]
        nome = produto["nome"]
        quant = produto["quant"]
        preco = produto["preco"]

        print(f"{cod} | {nome} | {quant} | {preco:.2f}€")

def converter_saldo(saldo):
    if isinstance(saldo, str):
        if 'e' in saldo or 'c' in saldo:
            euros = 0
            centimos = 0
            partes = saldo.split('e')
            if len(partes) > 1:
                euros = int(partes[0])
                centimos_part = partes[1].rstrip('c')
                if centimos_part:
                    centimos = int(centimos_part)
            else:
                centimos = int(partes[0].rstrip('c'))
            return euros + centimos / 100
        else:
            return float(saldo)
    elif isinstance(saldo, (int, float)):
        euros = int(saldo)
        centimos = round((saldo - euros) * 100)
        return f"{euros}e{centimos}c"
    else:
        raise ValueError("Formato de saldo inválido.")

def converter_saldo_para_cents(saldo_str):
    if 'e' in saldo_str or 'c' in saldo_str:
        euros = 0
        centimos = 0

        partes = saldo_str.split('e')
        if len(partes) > 1:
            euros = int(partes[0])  
            centimos_part = partes[1].rstrip('c')  
            if centimos_part:
                centimos = int(centimos_part)
        else:
            centimos = int(partes[0].rstrip('c'))
        return euros * 100 + centimos
    else:
        return int(float(saldo_str) * 100)

def moeda(tokens):
    # Verifica se há pelo menos um token de moeda após "MOEDA"
    if len(tokens) < 2 or not any(t.type in ["EUR", "CENT"] for t in tokens[1:]):
        print("maq: MOEDA <valor> (ex.: MOEDA 1e, 20c, 5c).")
        return 0

    cents = 0
    for t in tokens[1:]:
        if t.type == "EUR" or t.type == "CENT":
            cents += converter_saldo_para_cents(t.value)
    return cents

def tokenizar(texto):
    res = []

    lexer = lex.lex()
    lexer.input(texto)
    while True:
        tok = lexer.token()
        if not tok:
            break
        res.append(tok)

    return res

def selecionar(tokens, stock, cents):
    # Verifica se há um token para o código do produto
    if len(tokens) < 2 or tokens[1].type != "POSITION":
        print("maq: SELECIONAR <código> (ex.: SELECIONAR A23).")
        return None, cents

    codigo = tokens[1].value 
    produto_encontrado = None
    
    for produto in stock:
        if produto["cod"] == codigo:
            produto_encontrado = produto
            break
    
    if not produto_encontrado:
        print(f"maq: Produto com código '{codigo}' não encontrado.")
        return None, cents
    
    nome_produto = produto_encontrado["nome"]
    preco_cents = int(produto_encontrado["preco"] * 100) 
    quantidade = produto_encontrado["quant"]
    
    if quantidade <= 0:
        print(f"maq: Produto '{nome_produto}' está fora de stock.")
        return None, cents
    
    if cents < preco_cents:
        print(f"maq: Saldo insuficiente para '{nome_produto}'.\nmaq: Saldo = {cents // 100}e{cents % 100}c; Pedido = {preco_cents // 100}e{preco_cents % 100}c.")
        return None, cents

    produto_encontrado["quant"] -= 1 
    novo_saldo = cents - preco_cents  
    
    return nome_produto, novo_saldo

def calcular_troco(saldo_cents):
    moedas = [100, 50, 20, 10, 5, 2, 1]  
    troco = []
    
    for moeda in moedas:
        if saldo_cents >= moeda:
            quantidade = saldo_cents // moeda
            saldo_cents %= moeda
            if moeda >= 100:
                troco.append(f"{quantidade}x {moeda // 100}e")
            else:
                troco.append(f"{quantidade}x {moeda}c")
    
    return ", ".join(troco)

def saldo(cents):
    euros = cents // 100
    centimos = cents % 100
    return f"{euros}e{centimos}c"

def print_saldo(cents):
    print(f"maq: Saldo = {saldo(cents)}")

def main():
    print("maq: ON")
    try:
        with open("stock.json", "r", encoding="utf-8") as f:
            stock = json.load(f)["stock"]
            print("maq: Stock Atualizado")
    except FileNotFoundError:
        print("maq: Ficheiro 'stock.json' não encontrado.")
        return
    except json.JSONDecodeError:
        print("maq: Erro ao ler o ficheiro 'stock.json'. Verifique o formato.")
        return

    saldo_cents = 0
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        entrada = input(">> ").strip()
        if not entrada:
            print("maq: Erro, os comandos possíveis são: LISTAR, MOEDA, SELECIONAR, SAIR.")
            continue

        tokens = tokenizar(entrada)
        if not tokens:
            print("maq: Erro, os comandos possíveis são: LISTAR, MOEDA, SELECIONAR, SAIR.")
            continue

        comando = tokens[0].value.upper()

        if comando == "LISTAR":
            listar(stock)
        elif comando.startswith("MOEDA"):
            saldo_cents += moeda(tokens)
            print_saldo(saldo_cents)
        elif comando.startswith("SELECIONAR"):
            produto, saldo = selecionar(tokens, stock, saldo_cents)
            if produto:
                print(f"maq: Pode retirar o produto dispensado '{produto}'")
                saldo_cents = saldo
                print_saldo(saldo_cents)           
        elif comando == "SAIR":
            if saldo_cents > 0:
                troco = calcular_troco(saldo_cents)
                print(f"maq: Pode retirar o troco: {troco}.")
            print("maq: Até à próxima.")
            break
        else:
            print("maq: Comando inválido. Comandos disponíveis: LISTAR, MOEDA, SELECIONAR, SAIR.")

    try:
        with open("stock.json", "w", encoding="utf-8") as f:
            json.dump({"stock": stock}, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"maq: Erro ao salvar o stock: {e}")

if __name__ == "__main__":
    main()