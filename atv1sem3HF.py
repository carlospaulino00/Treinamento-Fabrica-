#Entrada
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
valor4 = int(input("Digite o quarto valor: "))

#Processamento
tupla_valores = (valor1, valor2, valor3, valor4)

contador_9 = tupla_valores.count(9)

posicao_3 = tupla_valores.index(3)

numeros_pares = [valor for valor in tupla_valores if valor % 2 == 0]

#Saida
print("Quantidade de vezes que o valor 9 apareceu:", contador_9)
print("Posição do primeiro valor 3:", posicao_3)
print("Números pares na tupla:", numeros_pares)