import random

#Entrada
numeros = tuple(random.randint(1, 100) for _ in range(5))

#Processamento 
print("Números gerados:")
for numero in numeros:
    print(numero)

menor_valor = min(numeros)
maior_valor = max(numeros)

#Saida
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)
