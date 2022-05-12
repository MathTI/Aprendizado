class Pessoa:
  def __init__(self,nome, idade)
    self.nome = nome
    self.idade = idade

  def setNome(self, nome):
    self.nome = nome

  def setIdade(self, idade):
    self.idade = idade
    
  def getNome(self):
    return self.nom

  def getIdade(self):
    return self.idade

Linha 1: A criação de uma classe começa pelo uso da palavra reservada class, seguida do nome da classe e dois pontos;

Linha 2: Aqui temos a definição do construtor da classe, que é um método especial chamado __init__. Como todo método em Python, sua declaração começa com def e entre parênteses estão os parâmetros, incluindo o parâmetro obrigatório self, que está presente em todos os métodos;

Linhas 3 e 4: O corpo do método deve estar identado, como manda a sintaxe da linguagem. Aqui estamos apenas atribuindo os valores recebidos por parâmetro aos atributos da classe;

Linhas 6 a 16: Criamos os métodos get e set de todos os atributos da classe Pessoa que serão responsáveis, respectivamente, por retornar ou modificar os atributos desta classe.
