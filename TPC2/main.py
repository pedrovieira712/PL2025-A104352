def ler_arquivo(nome_arquivo):
    # le o arquivo CSV e retorna uma lista de dicionários, onde cada dicionário representa uma obra.

    obras = []
    with open(nome_arquivo, 'r', encoding='utf-8') as ficheiro:
        cabecalho = ficheiro.readline().strip().split(';')  
        for linha in ficheiro:  
            valores = linha.strip().split(';') 

            if len(valores) == len(cabecalho):  
                obra = {}  #cria o dicionario
                for i, campo in enumerate(cabecalho):  #enumerate para saber o indice e valor
                    obra[campo] = valores[i]
                obras.append(obra)  
    return obras  

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