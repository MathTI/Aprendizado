def calcular_pagamento(qtd_horas, valor_hora):
  horas = float(qtd_horas)
  taxa = float(valor_hora)
  if horas <= 40:
    salario=horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario

horas = input('Quantidade de horas')
taxa = input('Valor/hora')
valor = calcular_pagamento(horas, taxa)
print(valor)

"""
Exemplo de uma função simples
n1 = input('Insira um valor: ')
n2 = input('Insira um valor: ')

def somar<---nome(n1, n2)<--- parâmetro/argumentos da função:
    soma<---variavel para somar = int(n1) + int(n2)
    print(soma) <--- função para exibir a soma
    return somar <--- retorna o valor para a função criada
somar(n1, n2)
"""