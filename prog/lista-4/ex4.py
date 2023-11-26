
contador = 0
quantidade = int(input())

while contador < quantidade:
    linha = input().split()
    palavra_1 = linha[0]
    palavra_2 = linha[1]
    final_palavra = ""
    contador2 = 0

    while contador2 < len(palavra_1) and contador2 < len(palavra_2):
        final_palavra += palavra_1[contador2] + palavra_2[contador2]
        contador2 += 1

    if contador2 < len(palavra_1):
        final_palavra+= palavra_1[contador2:]

    if contador2 < len(palavra_2):
        final_palavra += palavra_2[contador2:]
    

    print(final_palavra)
    contador += 1