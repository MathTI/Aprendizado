nome = input("Insira seu primeiro nome: ")

if nome.__len__() >= 4 and nome.__len__() <= 15:
    if nome.__len__() <= 6:
        print(f'{nome} é curto')
    elif nome.__len__() <= 8:
        print(f'{nome} é comum')
    elif nome.__len__() <= 12:
        print(f'{nome} é grande')
else:
    print("Insira 4 à 15 caracteres!!!")