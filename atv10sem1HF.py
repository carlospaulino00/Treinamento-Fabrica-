#Entrada
string = input("Digite uma frase: ")
palavra = input("Digite uma palavra para buscar na frase: ")
#Processamento
if palavra in string:
    #Saida
    print(True)
else:
    print(False)