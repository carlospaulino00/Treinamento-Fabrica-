import random

#Entrada
quantidade_jogos = int(input("Quantos jogos você deseja gerar? "))

jogos = []
#Processamento
for _ in range(quantidade_jogos):
    jogo = []
    for _ in range(5):
        numero = random.randint(1, 50)
        jogo.append(numero)
    jogos.append(jogo)

print("Palpites gerados:")
for jogo in jogos:
    #Saida
    print(jogo)
