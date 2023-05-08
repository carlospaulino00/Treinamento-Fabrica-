num1 = int(input("Digite o primeiro número: "))#Entrada
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))
#Processamento
maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num4 > maior:
    maior = num4
if num5 > maior:
    maior = num5

print("O maior número é:", maior)#Saida