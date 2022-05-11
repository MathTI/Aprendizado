"""len: verifica a quantidade de caracteres e pode ser usado para mais coisas. Obs: não funciona com int, float e booleano"""
usuario = input("insira o usuario: ")
caract_minimo = len(usuario)

print(len(usuario))  # função len chama o metodo len
print(usuario.__len__())  # metodo len
if caract_minimo < 6:
    print("Você precisa de 6 caracteres")
else:
    print("cadastrado")
