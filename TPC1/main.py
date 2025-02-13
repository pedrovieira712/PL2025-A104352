def process_text(text):
    soma = 0
    soma_ativa = True
    numero_atual = ''
    resultados = []
    i = 0

    while i < len(text):
        char = text[i]

        if char.isdigit():
            numero_atual += char
        elif char == '-' and i + 1 < len(text) and text[i + 1].isdigit():
            numero_atual = char

        else:
            if numero_atual and soma_ativa:
                soma += int(numero_atual)
            numero_atual = ''

            if i + 1 < len(text):
                if text[i:i + 2].lower() == 'on':
                    soma_ativa = True
                    i += 1
                elif i + 2 < len(text) and text[i:i + 3].lower() == 'off':
                    soma_ativa = False
                    i += 2

            if char == '=':
                resultados.append(soma)

        i += 1

    if numero_atual and soma_ativa:
        soma += int(numero_atual)
    resultados.append(soma)

    return resultados

texto = input("Introduza a frase pretendida: ").strip()
resultados = process_text(texto)

for resultado in resultados:
    print(resultado)