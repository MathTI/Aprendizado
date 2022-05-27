""" lambda é uma função anônima
Pode receber qualquer número de argumentos, mas pode ter apenas uma expressão
"""
func_soma = lambda valor: valor + 10
func_soma(1)

funcao_soma = lambda valor1, valor2: valor1 + valor2
valor1 = int(input("Valor: "))
valor2 = int(input("Valor: "))

print(funcao_soma(valor1, valor2))

exemplo = lambda valor: "Verdadeiro" if valor % 2 == 0 else "Falso"
print(exemplo(4))

