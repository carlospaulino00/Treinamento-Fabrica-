from datetime import date

ano_atual = date.today().year

maiores_idade = 0
menores_idade = 0

for i in range(1, 8):
    #Entrada
    ano_nasc = int(input(f"Digite o ano de nascimento da pessoa {i}: "))

    #Processamento 
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1

#Saida
print(f"\n{maiores_idade} pessoas atingiram a maioridade.")
print(f"{menores_idade} pessoas ainda não atingiram a maioridade.")