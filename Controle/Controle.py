class ControleRemoto:
    altura: int  # Typecasting serve para deixar mais claro sobre a variável
    largura: int
    profundidade: int
    cor: str

    def __init__(self, altura, largura, profundidade, cor):
        self.altura = altura  # self.altura é a caracteristica e altura é a variável, ou seja, ao atribuir um valor a variável altura se tornara a caract
        self.largura = largura
        self.profundidade = profundidade
        self.cor = cor

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar")
        elif botao == "-":
            print("Diminuir")

Controle1 = ControleRemoto(5, 3,3, "preto")
Controle1.passar_canal("+")