from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor
    
    def dar_aumento(self, percentual):
        aumento = self.salario * percentual / 100
        self.salario += aumento
        print("Aumento de salário concedido.")
