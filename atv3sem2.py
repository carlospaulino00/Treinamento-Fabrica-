import random

#Entrada
opcao = ["pedra", "papel", "tesoura"]
computador = random.choice(opcao)

jogador = input("Escolha pedra, papel ou tesoura: ").lower()

#Processamento
if jogador == computador:
    #Saida
    print("Empate!")
elif jogador == "pedra":
    if computador == "papel":
        print("Você perdeu! Papel cobre pedra.")
    else:
        print("Você ganhou! Pedra quebra tesoura.")
elif jogador == "papel":
    if computador == "tesoura":
        print("Você perdeu! Tesoura corta papel.")
    else:
        print("Você ganhou! Papel cobre pedra.")
elif jogador == "tesoura":
    if computador == "pedra":
        print("Você perdeu! Pedra quebra tesoura.")
    else:
        print("Você ganhou! Tesoura corta papel.")
else:
    print("Escolha inválida. Tente novamente!")