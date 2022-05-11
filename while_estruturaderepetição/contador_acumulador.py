contador = 0
acumulador = 0

while contador <= 10:
    print(f'Contador: {contador}')  #  contador só faz a contagem
    acumulador += contador
    contador += 1
    print(f'Acumulador: {acumulador}')  # acumulador acumula a cada lanço
else:  # No python podemos utilizar o else no laço while
    print('Finish')