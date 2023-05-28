
lista_valores = []


while True:
    #Entrada
    valor = int(input("Digite um valor (digite 0 para sair): "))

    #Processamento
    if valor == 0:
        break

    if valor not in lista_valores:
        lista_valores.append(valor)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado. Não será adicionado.")

lista_valores.sort()

#Saida
print("Valores únicos em ordem crescente:")
for valor in lista_valores:
    print(valor)
