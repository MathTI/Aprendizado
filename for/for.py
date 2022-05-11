"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

texto= 'Python'
n = ''  # Lista vazia para iterar as letras
"""
for numero in range(0, 100, 8):
    print(numero)

for numero in range(100):
    if numero % 8 == 0:
        print(numero)
"""
for letra in texto:  # Vai passar por cada elemento que tem na variável texto
    if letra == 't':  # vai checar se elemento letra é igual a 't'
        n += letra.upper()  # Adiciona elemento na nova lista modificando a letra 't'
    elif letra == 'h':
        n += letra.upper()  # aAdiciona elemento na nova lista modificando a letra 'h'
    else:
        n += letra  # Vai adicionar o elemento dentro da nova lista
print(n)

