class Clientes:
    def __init__(self, nome, email, plano):
        self.nome = nome  # self.nome é a caracteristica e nome é a variável
        self.email = email
        self.plano = plano
        self.planos = ['Basic', 'Premium']  # self.planos é a característica do cliente que está recebendo um valor constante
        if  plano in self.planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos:
            self.plano = novo_plano
        else:
            print('Plano inválido')

    def ver_filme(self,filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver filme {filme}")
        elif self.plano == 'Premium':
            print(f"Ver filme{filme}")
        elif self.plano == 'Basic' and plano_filme == 'Premium':
            print("Faça upgrade para premium")
        else:
            print('Plano inválido')

cliente = Clientes(input("Digite o nome: "), input("Digite email: "), input("Digite o plano: "))
print(cliente.plano)
cliente.ver_filme("Harry potter", "Premium")
# Botão de upgrade ou deegrade
cliente.mudar_plano("Premium")
print(cliente.plano)
cliente.ver_filme("Harry potter", "Premium")
#  Exemplo de código que salva no banco de dados: Clientes.add_to_database
# def adicionar_cliente_no_bd(self):