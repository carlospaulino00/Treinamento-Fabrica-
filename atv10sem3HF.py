jogador = {}
#Entrada
nome = input("Digite o nome do jogador: ")
jogador['nome'] = nome

quantidade_partidas = int(input("Digite a quantidade de partidas jogadas: "))
jogador['partidas_jogadas'] = quantidade_partidas
#Processamento
gols_por_partida = []
for partida in range(1, quantidade_partidas + 1):
    gols = int(input(f"Digite a quantidade de gols feitos na partida {partida}: "))
    gols_por_partida.append(gols)

total_gols = sum(gols_por_partida)
jogador['gols_por_partida'] = gols_por_partida
jogador['total_gols'] = total_gols
#Saida
print("\nAproveitamento do jogador:")
print("Nome:", jogador['nome'])
print("Partidas jogadas:", jogador['partidas_jogadas'])
print("Gols por partida:", jogador['gols_por_partida'])
print("Total de gols:", jogador['total_gols'])
