import random

vitorias_consecutivas = 0

while True:

    while True:
        #Entrada
        jogador_escolha = input('Escolha PAR ou ÍMPAR: ').strip().upper()
        #Processamento
        if jogador_escolha in ['PAR', 'IMPAR']:
            break
        else:
            print('Opção inválida. Tente novamente.')

    while True:
        #Entrada
        jogador_numero = int(input('Digite um número de 0 a 10: '))
        #Processamento
        if jogador_numero >= 0 and jogador_numero <= 10:
            break
        else:
            print('Número inválido. Tente novamente.')

    
    computador_numero = random.randint(0, 10)

    soma = jogador_numero + computador_numero

    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'

    print(f'Você jogou {jogador_numero} e o computador jogou {computador_numero}. Total de {soma} deu {resultado}')

    if resultado == jogador_escolha:
        print('Você VENCEU!')
        vitorias_consecutivas += 1
    else:
        print('Você PERDEU!')
        break
#Saida
print(f'GAME OVER! Você venceu {vitorias_consecutivas} vezes.')
