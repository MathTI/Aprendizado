"""Cálculdora básica"""

valor1 = input('Digite um número: ')
operacao = input('Digite a operação: ')
valor2 = input('Digite um número: ')

if 'x' or '*' in operacao:
    print(int(valor1) * int(valor2))
elif '+' in operacao:
    print(int(valor1) + int(valor2))
elif '-' in operacao:
    print(int(valor1) - int(valor2))
elif '/' in operacao:
    print(int(valor1) / int(valor2))


