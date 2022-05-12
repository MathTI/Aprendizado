from pessoa import Pessoa

class PessoaFisica(Pessoa):
   def __init__(self, CPF, nome, idade):
       super().__init__(nome, idade)
       self.CPF = CPF

   def getCPF(self):
       return self.CPF

   def setCPF(self, CPF):
       self.CPF = CPF
      
Linha 1: Como vamos herdar da classe Pessoa e ela foi definida em outro arquivo (pessoa.py), precisamos importá-la. Para isso usamos a instrução import e indicamos o nome
do arquivo, sem a extensão .py, seguido do nome da classe que queremos importar;
Linha 3: Para definir que uma classe herdará de uma outra classe, precisamos indicar o nome da classe pai entre parênteses após o nome da classe filha;
Linha 4: Criamos o construtor da classe filha e definimos quais atributos ela espera receber. Neste caso, o nome e idade estão definidos na classe pai, enquanto o cpf é 
próprio da classe filha;
Linha 5: Utilizando o método super, invocamos o construtor da classe pai. Com isso aproveitamos todo a lógica definida nesse método, que no caso faz a atribuição dos valo-
res de nome e idade aos atributos da classe. Com isso garantimos que ao ser criada, a classe filha efetuará o mesmo processamento que a classe pai e mais alguns passos adicionais.
