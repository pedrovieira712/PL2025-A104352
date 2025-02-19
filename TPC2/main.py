def ler_arquivo(nome_arquivo):
    # lê o arquivo CSV e retorna uma lista de dicionários, onde cada dicionário representa uma obra.
    obras = []
    linha_temporaria = ""
    dentro_de_aspas = False

    with open(nome_arquivo, "r", encoding="utf-8") as ficheiro:
        cabecalho = ficheiro.readline().strip().split(';')  # primeira linha que contem info de cada ;

        for linha in ficheiro:
            linha = linha.strip()

            if dentro_de_aspas:
                linha_temporaria += " " + linha
                if linha.count('"') % 2 != 0:   
                    dentro_de_aspas = False
                    obras.append(processar_linha(linha_temporaria, cabecalho))
                    linha_temporaria = ""
                continue

            if linha.count('"') % 2 != 0:
                dentro_de_aspas = True
                linha_temporaria = linha
                continue

            if linha:
                obras.append(processar_linha(linha, cabecalho))

    return obras


def processar_linha(linha, cabecalho):
    campos = []
    campo_atual = ""
    dentro_de_aspas = False

    for char in linha:
        if char == '"':  
            dentro_de_aspas = not dentro_de_aspas
        elif char == ";" and not dentro_de_aspas:  
            campos.append(campo_atual.strip())
            campo_atual = ""
        else:
            campo_atual += char  

    campos.append(campo_atual.strip())  
    return {cabecalho[i]: campos[i] for i in range(len(cabecalho))}

def lista_compositores(obras):
    # Retorna uma lista ordenada alfabeticamente de compositores únicos a partir da lista de obras.
    compositores = set()  
    for obra in obras:
        compositores.add(obra['compositor'])   

    return sorted(compositores)   


def distribuicao_por_periodo(obras):
    # retorna dicionario com a contagem de quantas obras pertencem a cada período musical.
    distribuicao = {}   
    for obra in obras:
        periodo = obra['periodo'] 
        distribuicao[periodo] = distribuicao.get(periodo, 0) + 1  
    return distribuicao  


def titulos_por_periodo(obras):
    # junta os títulos das obras por período musical ordena alfabeticamente e retorna o dicionario com os periodos como cahve e os titulos como valores
    periodos = {} 
    for obra in obras:
        periodo = obra['periodo']  
        titulo = obra['nome']  
        if periodo not in periodos:
            periodos[periodo] = []
        periodos[periodo].append(titulo)   

    for periodo in periodos:
        periodos[periodo] = sorted(periodos[periodo])

    return periodos   

def main():
    obras = ler_arquivo('obras.csv')
    
    # 1. Lista ordenada alfabeticamente dos compositores musicais
    print("-> Compositores")
    for compositor in lista_compositores(obras):
        print(compositor)

    # 2. Distribuição das obras por período musical
    print("\n-> Distribuição por Período")
    for periodo, quantidade in distribuicao_por_periodo(obras).items():
        print(f"{periodo}: {quantidade} obras")

    # 3. Exibe os títulos das obras organizados por período
    print("\n-> Títulos por Período") 
    for periodo, titulos in titulos_por_periodo(obras).items():
        print(f"\n{periodo}:")
        for titulo in titulos:
            print(f"  - {titulo}")

if __name__ == "__main__":
    main()