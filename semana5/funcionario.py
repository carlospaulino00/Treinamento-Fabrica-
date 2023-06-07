class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def imprimir_informacoes(self):
        print("Nome:", self.nome)
        print("Salário:", self.salario)
