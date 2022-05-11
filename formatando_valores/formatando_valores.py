"""
Formatando valores com modificadores

:s - Texto (str)
:d - Inteiro (int)
:f - ponto flutuante (float)
:. (numero)f - quantidade de casas decimais (float)
: (caractere) (> direita; < esquerda; ^ centro (tipo - s, d ou f)
"""
n = 1
n1 = 3
n2 = "Matheus lima"
n_formatado = '{n3:0^20}'.format(n3=n2)
print(f'{n:0^10}')
print(f'{n:0>10}')
print(f'{n:0<10}')
print(f'{n:f}')
print(n_formatado)
print('{0:s^3} {1:#^3}'.format(n, n1))
