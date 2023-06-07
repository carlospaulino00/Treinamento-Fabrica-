class ContaBancaria:
    def __init__(self, nome_titular, numero_conta, saldo=0):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")
    
    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
