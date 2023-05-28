numeros = []

for i in range(5):
    #Entrada
    numero = int(input(f"Digite o {i+1} número: "))
    numeros.append(numero)
#Processamento
numeros_ordenados = sorted(numeros)

#Saida
print("Lista ordenada:", numeros_ordenados)