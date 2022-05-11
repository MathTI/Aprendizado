"""Formatação de strings"""

nome = "Matheus"
idade = 25
altura = 1.78
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e tem o imc de', imc)
print(f'{nome} tem {idade} anos de idade e tem o imc de {imc:.2f}')  # Formatação da string. Podemos notar que o :.2f é para arredondar até 2 casas decimais
print('{} tem {} anos de idade e tem o imc de {:.2f}'.format(nome, idade, imc))  # Outra maneira de formatar a string.
print('{0} tem {1} anos de idade e tem o imc de {2:.2f}'.format(nome, idade, imc))  # Notamos que nesse formato cada variável tem um indice
print('{n} tem {i} anos de idade e tem o imc de {im:.2f}'.format(n=nome, i=idade, im=imc))  # Nesse formato podemos alterar os parâmetros nomeados
