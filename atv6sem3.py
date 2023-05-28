numeros = []
pares = []
impares = []

for i in range(10):
    #Entrada
    numero = int(input(f"Digite o {i+1} número: "))
    numeros.append(numero)

#Processamento
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

#Saida
print("Lista completa:", numeros)
print("Valores pares:", pares)
print("Valores ímpares:", impares)
