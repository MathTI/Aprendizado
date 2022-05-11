num1 = input("Digite um número")
"""
if num1.isdigit():
    num1 = int(num1)
    if num1 % 2 == 0:
        print("Número par")
    else:
        print("Número impar")
else:
    print("Somente números")
"""
if not num1.isdigit():
    print("Não é um número inteiro")
else:
    num1 = int(num1)
    if not num1 % 2 == 0:
        print("É impar")
    else:
        print("É par")