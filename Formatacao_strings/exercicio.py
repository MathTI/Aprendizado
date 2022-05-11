"""
*Criar variáveis para nome (str), idade (int), altura (float) e peso(float)  de uma pessoa
*Criar variável com o ano atual (int)
*Obter o ano de nascimento da pessoa (baseado na idade e ano atual)
*Obter o imc da pessoa com 2 casas decimais
*Exibir um texto com todos os valores na tela usando f-strings(com chaves)
"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / (altura**2)

print(f'{nome} nasceu em {ano_nascimento}, tem {idade} anos, sua altura é de {altura} com o imc de {imc:.2f}')