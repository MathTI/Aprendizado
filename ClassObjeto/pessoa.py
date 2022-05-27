"""Python é uma linguagem de programação orientada a objetos
Quase tudo em python é um objeto, com suas propriedades e métodos
Uma Classe é como um construtor de objetos, ou um 'projeto' para criar objetos"""


class Pessoa:
    Nome: str
    Idade: int
    #  Caracteristicas são criadas na função init
    def __init__(self, Nome, Idade):  #
        self.Nome = Nome  # caracteristica
        self.Idade = Idade # caracteristica

    # função de boas vindas
    def Boas_vindas(self):
        print('Bem vindo', self.Nome)

    # função de restrição
    def Recusado(self):
        print('Seu acesso foi recusado!!!')

    # funçao. Aqui é aplicada a regra de negócio
    def Maior_idade(self):
        if self.Idade >= 18:
            print("Maior de idade")
            self.Boas_vindas()
        else:
            print('Menor de idade')
            self.Recusado()
dados = Pessoa(input("Digite o nome: "), int(input("Digite a idade: ")))
dados.Maior_idade()


