
def leiaInt(mensagem):
    while True:
        try:
            #Entrada
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")
#Processamento
n = leiaInt('Digite um número: ')
#Saida
print("O número digitado é:", n)
