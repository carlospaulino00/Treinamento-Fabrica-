num1 = int(input("Digite o primeiro número: "))#Entrada
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 == num2 == num3:#Processamento
    print("Três iguais")#Saida
elif num1 != num2 and num1 != num3 and num2 != num3:
    print("Três diferentes")
else:
    print("Dois iguais")