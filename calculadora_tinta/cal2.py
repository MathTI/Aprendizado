altura: float = 2.9
x = 0

while True:
    op = input('Digite [p] para cálcular área da parede ou [t] para área do teto: ')
    if op == 'p':
        largura = input('Digite a largura: ')
        profundidade = input('Digite a profundidade: ')
        if largura.isdigit() and profundidade.isdigit():
            largura = float(largura)
            profundidade = float(profundidade)
            print(f'Litros para parede: {2 * (largura + profundidade) * altura}')
            sair = input('Desejar sair? [s]im ou [n]ão: ')
            if sair == 's':
                break
    elif op == 't':
        largura = input('Digite a largura: ')
        profundidade = input('Digite a profundidade: ')
        if largura.isdigit() and profundidade.isdigit():
            largura = float(largura)
            profundidade = float(profundidade)
            print(f'Litros para o teto: {largura * profundidade}')
            sair = input('Desejar sair? [s]im ou [n]ão: ')
            if sair == 's':
                break