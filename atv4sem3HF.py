lista_numeros = []

while True:
    #Entrada
    numero = int(input("Digite um número (digite 0 para sair): "))

    #Processamento
    if numero == 0:
        break

    lista_numeros.append(numero)
quantidade_numeros = len(lista_numeros)

lista_numeros.sort(reverse=True)

valor_5_presente = 5 in lista_numeros

#Saida
print("Quantidade de números digitados:", quantidade_numeros)
print("Lista de valores em ordem decrescente:", lista_numeros)
if valor_5_presente:
    print("O valor 5 está na lista.")
else:
    print("O valor 5 não está na lista.")
