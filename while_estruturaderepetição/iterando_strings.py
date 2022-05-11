#  indices [01234...33]

frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
contador = 0
frase1 = ''

while contador < tamanho:
    letra = frase[contador]
    if letra == 'r':
        frase1 += 'R'
    else:
        frase1 += frase[contador]
    contador += 1
    print(frase1)  # mostra iteração
print(frase1)  # mostra a frase final