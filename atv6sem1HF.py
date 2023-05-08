import datetime

ano_nascimento = int(input("Digite o ano de nascimento: "))#Entrada

#Processamento
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento

if idade >= 18:
    print("Você é maior de idade!")#Saida
else:
    print("Você é menor de idade.")