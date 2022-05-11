"""Método construtor: """
class Comodo:
    __largura: float
    __profundidade: float
    __altura: float
    def __init__(self, largura, profundidade):
        self.largura = largura
        self.profundidade = profundidade
        self.__altura = 2.9

    @property  # O decorator indica @Property indica que o método imediamente abaixo se trata de uma propriedade
    def largura (self):  # O método vai ser acessado como um atributo. valor = comodo.largura
        return self.__largura

    @property
    def profundidade (self):
        return self.__profundidade

    @property
    def altura (self):
        return self.__altura

    @largura.setter  # recebe o valor da largura
    def largura(self, largura):  # declara metodo largura e parâmetro largura
        try:
            self.__largura = float(largura)  # adiciona atributo que recebe como parâmetro ao atributo da classe
        except Exception:
            print('Valor inválido')
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)
        except Exception:
            print('Valor inválido')
            exit()
