from datetime import datetime

ano_atual = datetime.now().year

def calcular_idade(ano_nascimento):
    return ano_atual - ano_nascimento

def calcular_aposentadoria(ano_contratacao):
    idade_aposentadoria = 65
    anos_contribuicao = ano_atual - ano_contratacao
    anos_restantes = idade_aposentadoria - anos_contribuicao
    if anos_restantes <= 0:
        return "Já está aposentado(a)"
    else:
        return ano_atual + anos_restantes

pessoas = []

while True:
    #Entrada
    pessoa = {}
    pessoa['nome'] = input("Digite o nome da pessoa (ou digite 'sair' para encerrar): ")
    
    #Processamento
    if pessoa['nome'].lower() == 'sair':
        break
    
    pessoa['ano_nascimento'] = int(input("Digite o ano de nascimento da pessoa: "))
    pessoa['ctps'] = int(input("Digite o número da carteira de trabalho da pessoa: "))

    if pessoa['ctps'] != 0:
        pessoa['ano_contratacao'] = int(input("Digite o ano de contratação: "))
        pessoa['salario'] = float(input("Digite o salário: "))

        pessoa['aposentadoria'] = calcular_aposentadoria(pessoa['ano_contratacao'])

    pessoa['idade'] = calcular_idade(pessoa['ano_nascimento'])

    pessoas.append(pessoa)
#Saida
print("Dados das pessoas:")
for pessoa in pessoas:
    print("Nome:", pessoa['nome'])
    print("Idade:", pessoa['idade'])
    if pessoa['ctps'] != 0:
        print("CTPS:", pessoa['ctps'])
        print("Ano de contratação:", pessoa['ano_contratacao'])
        print("Salário:", pessoa['salario'])
        print("Previsão de aposentadoria:", pessoa['aposentadoria'])
    print()

