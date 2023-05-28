import random

def lancar_dado():
    return random.randint(1, 6)

resultados = {}

for jogador in range(1, 5):
    #Entrada
    resultado = lancar_dado()
    resultados[f"Jogador {jogador}"] = resultado

#Processamento
resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)


print("Resultados do jogo:")
#Saida
for jogador, resultado in resultados_ordenados:
    print(f"{jogador}: {resultado}")

vencedor = resultados_ordenados[0][0]
print(f"\nO vencedor do jogo é: {vencedor}")
