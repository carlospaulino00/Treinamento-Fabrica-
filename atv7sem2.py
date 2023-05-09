#Entrada
sexo = input("Digite o sexo (M/F): ").upper()
#Processamento
while sexo != "M" and sexo != "F":
    sexo = input("Entrada inválida. Digite o sexo novamente (M/F): ").upper()
#Saida
print("Sexo digitado:", sexo)
