valores = []
pares = []
impares = []

for i in range(5):
    #Entrada
    numero = int(input(f"Digite o {i+1} número: "))
    valores.append(numero)

#Processamento
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

pares.sort()
impares.sort()
#Saidaprint("Valores pares em ordem crescente:", pares)
print("Valores ímpares em ordem crescente:", impares)

