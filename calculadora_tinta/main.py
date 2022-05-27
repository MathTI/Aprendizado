from calculadora import Calculadora  # importando classe
from comodo import Comodo

calc = Calculadora()  # criando objeto da classe calculadora

comodo = Comodo(
    input('Digite a largura: '),
    input('Digite a profundidade: '))

#calc.area_parede: float = 2*(largura + profundidade) * altura  Obs:

print(f'A área das paredes é: {calc.calcular_area_parede(comodo)}')

print(f'A área do teto é: {calc.calcular_teto(comodo)}')

print(f'A litragem de tinta necessária é: {calc.calcular_litragem()}')
