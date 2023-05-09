import datetime
#Entrada
ano_atual = datetime.datetime.now().year
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
#Processamento
idade = ano_atual - ano_nascimento

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
#Saida
print(f'O atleta tem {idade} anos e se enquadra na categoria {categoria}.')