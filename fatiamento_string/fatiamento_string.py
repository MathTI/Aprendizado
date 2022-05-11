"""
Fatiamento é devisão da string
"""
texto = "Strings podem ser separadas pelo fatiamento"
texto2 = "Matheus"

print(texto[:13])  # elas tem indices e podemos seleciona-los. Nesse caso o inicio(0) foi ocultado
print(texto[0:13])  # elas tem indices e podemos seleciona-los
print(texto[0::2])  # elas tem indices, podemos selecionar onde vai começar, terminar e a pausa
print(texto[0:20:2])  # elas tem indices, podemos selecionar onde vai começar, terminar, intervalo e o máximo de strings
print(f'{texto[38]}{texto[0]}')

for letra in texto2:
    print(letra)