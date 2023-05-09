soma = 0
qtd = 0
maior = menor = 0

while True:
    #Entrada
    num = int(input("Digite um número inteiro: "))
    #Processamento
    soma += num
    qtd += 1

    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    opcao = input("Deseja continuar? [S/N] ").strip().upper()
    if opcao != "S":
        break

media = soma / qtd
#Saida
print(f"Média: {media:.2f}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")