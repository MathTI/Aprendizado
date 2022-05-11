"""
while: usado par realizar ações enquanto uma condição for verdadeira
obs: for também é uma estrutura de repetição, assim como while
requisitos: Entender condições e operações
"""
x = 0
while x < 10:  # loop infinito
  if x == 3:  # iria relacionar x a 3
    x += 1  # Para que na próxima checagem não fique preso nesse bloco
    #  break: Quebra o lanço de repetição, ou seja, while para de ser executado
    continue  # essa palavras reservada faz com que os códigos dentro da mesma estrutura não sejam executados
  print(x)  # loop infinito
  x += 1  # Adicionando um valor que faz a condicao do while ser falsa quebra o loop infito
  print(x)
print(" Aqui está fora do bloco while e não será executado a não ser que while seja falso")