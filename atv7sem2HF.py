import random

numero_aleatorio = random.randint(0, 10)  # escolhe um número aleatório entre 0 e 10
palpite = -1  # inicializa o palpite do jogador com um valor inválido
num_tentativas = 0  # inicializa o número de tentativas com zero

while palpite != numero_aleatorio:
    #Entrada
    palpite = int(input("Digite um número entre 0 e 10: "))  # solicita o palpite do jogador
    num_tentativas += 1  # incrementa o número de tentativas
    #Processamento
    if palpite < numero_aleatorio:
        print("O número é maior")
    elif palpite > numero_aleatorio:
        print("O número é menor")
#Saida
print("Você acertou o número em", num_tentativas, "tentativas.")
