"""
operadores lógicos
and: compara se ambas comparações são verdeiras
or: verifica se uma é verdadeira
not: inverte o valor
in: dentro
not in: não dentro
"""
# exemplos

a = 1
b = 2
c = 3
d = ''

if a < c and a!=b:
    print("Menor")
elif not c > b:
    print("Not")
elif not d:
    print("preencha o valor de d")  # se a variavel estiver vazia ou com 0 vai executar esse comando após checar os demais
