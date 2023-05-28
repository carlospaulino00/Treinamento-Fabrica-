lista_numeros = []

while True:
    #Entrada
    numero = int(input("Digite um número (digite 0 para sair): "))

    #Processamento
    if numero == 0:
        break

    lista_numeros.append(numero)

lista_pares = []
lista_impares = []

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

#Saida
print("Lista completa de números:", lista_numeros)
print("Lista de números pares:", lista_pares)
print("Lista de números ímpares:", lista_impares)