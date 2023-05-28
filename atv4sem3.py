numeros = []

for i in range(5):
    #Entrada
    numero = int(input(f"Digite o {i+1} número: "))
    numeros.append(numero)
#Processamento
menor_valor = min(numeros)
maior_valor = max(numeros)

posicao_menor = numeros.index(menor_valor)
posicao_maior = numeros.index(maior_valor)

#Saida
print(f"Menor valor digitado: {menor_valor}")
print(f"Posição na lista: {posicao_menor}")
print(f"Maior valor digitado: {maior_valor}")
print(f"Posição na lista: {posicao_maior}")
