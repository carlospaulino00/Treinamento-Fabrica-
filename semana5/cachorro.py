from animal import Animal

class Cachorro(Animal):

    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print('auau')

    def apresentar(self):
        print(f'ola meu nome é {self.nome} tenho {self.idade} anos e sou da raça {self.raca}')