#Entrada
frase = input("Digite uma frase: ")
frase = frase.replace(" ", "")
palindromo = True
#Processamento
for i in range(len(frase)):
    if frase[i] != frase[-i-1]:
        palindromo = False
        break

if palindromo:
    #Saida
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")