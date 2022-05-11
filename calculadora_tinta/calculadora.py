class Calculadora:
    __area_parede: float  # atributos
    __area_teto: float

    def calcular_area_parede(self, comodo):  # Criando uma função de uma classe. O parâmetro self é obrigatório,pois, dá
# acesso as informações dentro de uma classe
        self.__area_parede = 2*(comodo.largura + comodo.profundidade) * comodo.altura  # É um atributo, não uma variável
        return self.__area_parede

    def calcular_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade  # É um atributo, não uma variável
        return self.__area_teto

    def calcular_litragem(self):
        if self.__area_parede or self.__area_teto <= 0:
            print("Não é possível calcular a litragem com os valores informados")
            exit()
        return (self.__area_parede + self.__area_teto) / 10
