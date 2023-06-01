import random

def sorteia():
    numeros = []
    for _ in range(5):
        #Entrada
        numeros.append(random.randint(1, 10))
    return numeros
#Processamento
def somaPar(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    return soma
#Saida
lista_numeros = sorteia()
print("Números sorteados:", lista_numeros)

resultado = somaPar(lista_numeros)
print("Soma dos números pares:", resultado)
