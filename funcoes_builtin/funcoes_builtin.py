num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
print(id(num1))

# isdigit isnumeric isdecimal checa se são números
# Nesse caso é necessário converter os inputs dentro do bloco if

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
    print(id(num1))
else:
    print("somente números")

"""
Tenta executar o bloco. Caso ocorrá um erro pula para bloco de baixo sem aparecer o erro
try:
num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
except:
    print("somente números")
"""