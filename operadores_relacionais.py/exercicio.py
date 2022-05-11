usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")
base_usuario = "maxz14" or "teteu" or "mat"
base_senha = "123" or "111" or "222"

if usuario == base_usuario and senha == base_senha:
    print(f"bem vindo {usuario}")
else:
    print("usuario e senha errados. Tente novamente")