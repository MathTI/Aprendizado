import random

lista = [1, 2, 3, 4, 5]
palavra = "Sorte"
Nomes = ['Matheus', 'Kelayne', 'Karol', 'Rafael', 'Kelly', 'Welligton', 'Felipe']

print(random.choice(lista))  # Sorteia um número da lista
print(random.choice(palavra))  # Consegue sortear letra da string
print(random.choice(Nomes))  # Consegue sortear os itens da lista. Sejam eles strings ou outra variavel basica
print(random.random())  # Gera um número aleatório de  0 - 1
print(random.randint(0, 100))  # Gera um número aleatório de  0 - 100
