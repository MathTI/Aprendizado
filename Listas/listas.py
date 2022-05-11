"""Lista é uma coleção de valores indexada, em que cada valor é identificado por um índice.O primeiro item na lista está no índice 0,
o segundo no índice 1 e assim por diante. Ela é mutável e tem como modificar, adicionar ou remover um item"""

lista = ['Matheus', 'Lucas', 'Valter', 'Luiz', 'Rodrigo', 'Willians']
lista[0] = 'Matheus lima'  # Alterando item da lista pelo indice
lista.append('Henrique')  # Adiciona um novo item
lista.insert(7, 'Kelayne')  # Adiciona item e escolhe a posição
lista.pop(7)  # remove item pelo indice da lista
lista.remove('Henrique')  # remove o item pelo elemento da lista
del(lista[3:5])

print(lista)