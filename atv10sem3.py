import random

jogadores = ['Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4']

resultados = {}
#Entrada
for jogador in jogadores:
    resultado = random.randint(1, 6)
    resultados[jogador] = resultado
#Processamento
print("Resultados dos jogadores:")
for jogador, resultado in resultados.items():
    print(jogador + ":", resultado)

resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)
#Saida
print("\nClassificação final:")
for i, (jogador, resultado) in enumerate(resultados_ordenados):
    print(f"{i+1} lugar: {jogador} - {resultado}")