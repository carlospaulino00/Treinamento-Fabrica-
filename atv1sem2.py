#Entrada
valor_casa = float(input("Qual é o valor da casa? R$ "))
salario = float(input("Qual é o seu salário? R$ "))
anos = int(input("Em quantos anos você deseja pagar? "))

prestacao_mensal = valor_casa / (anos * 12) 
limite_prestacao = salario * 0.3 

#Processamento
if prestacao_mensal <= limite_prestacao:
    #Saida
    print("Empréstimo aprovado!")
    print("Valor da prestação mensal: R$ {:.2f}".format(prestacao_mensal))
else:
    print("Empréstimo negado.")
    print("Valor da prestação mensal excede 30% do salário.") 