""" Entrada de dados"""

nome = input("Digite seu usuário: ")  # comando input é usado para que seja possível o usuário inserir dados
peso = float(input("Digite o peso: "))  # Para fazer cálculos é necessário fazer o type casting, pois, tudo inserido no input é uma str
altura = float(input("Digite a altura: "))  # Para fazer cálculos é necessário fazer o type casting
imc = peso / (altura**2)  # Para fazer cálculos é necessário fazer o type casting. Podemos aplicar ele diretamente no input ou na formula
print(f'Seu nome é {nome} e seu imc é {imc}')
print(f'O tipo da variável nome é {type(nome)} e da variável imc é {type(imc)}')
print(f'Cálculo de imc = {peso / (altura**2):.2f}')
