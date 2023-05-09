import datetime

ano_atual = datetime.datetime.now().year
#Entrada
ano_nascimento = int(input("Digite o ano de nascimento do jovem: "))
idade = ano_atual - ano_nascimento
#Processamento
if idade < 18:
    anos_falta = 18 - idade
    #Saida
    print(f"O jovem tem {idade} anos e ainda vai se alistar ao serviço militar.")
    print(f"Falta(m) {anos_falta} ano(s) para o alistamento.")
elif idade == 18:
    print(f"O jovem tem {idade} anos e é hora de se alistar ao serviço militar.")
else:
    anos_passou = idade - 18
    print(f"O jovem tem {idade} anos e já passou do tempo de alistamento.")
    print(f"Passou {anos_passou} ano(s) do prazo de alistamento.")
