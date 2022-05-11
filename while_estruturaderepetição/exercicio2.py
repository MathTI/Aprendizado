while True:
    print()
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    op = input("Digite um operador: ")
    print()
    if not num1.isnumeric() or not num2.isnumeric():
        print()
        print("Digite um número")
        continue
    num1 = int(num1)
    num2 = int(num2)
    sair = input('Desejar sair? [s]im ou [n]ão')
    if sair == 's':
        break
    if op == 'x':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    elif op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
