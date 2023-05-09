soma_idade = 0
maior_idade_homem = 0
nome_homem_velho = ''
mulheres_menos_20 = 0

for i in range(4):
    #Entrada
    print(f'---- {i+1}ª Pessoa ----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper()

    #Processamento
    soma_idade += idade

    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_velho = nome
    
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idade / 4

#Saida
print(f'A média de idade do grupo é {media_idade:.1f} anos')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_homem_velho}')
print(f'{mulheres_menos_20} mulheres tem menos de 20 anos')
