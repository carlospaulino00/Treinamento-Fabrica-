maior_peso = 0
menor_peso = 0


for i in range(1, 6):
    #Entrada
    peso = float(input(f"Digite o peso da pessoa {i}: "))
    
    #Processamento
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

#Saida
print(f"O maior peso lido foi {maior_peso} kg")
print(f"O menor peso lido foi {menor_peso} kg")