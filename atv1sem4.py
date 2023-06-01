#Processamento
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

#Entrada
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

s = soma(a, b)
sub = subtracao(a, b)
mult = multiplicacao(a, b)
#Saida
print("A soma de a e b é:", s)
print("A subtração de a por b é:", sub)
print("A multiplicação de a por b é:", mult)
