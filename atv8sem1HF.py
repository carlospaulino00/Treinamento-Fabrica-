#Entrada
frase = "treinamento hoje de backend"
palavra_antiga = input("Digite a palavra a ser substituída: ")
palavra_nova = input("Digite a palavra nova: ")

frase_modificada = frase.replace(palavra_antiga, palavra_nova)#Processamento

#Saida
print("Frase original: ", frase)
print("Frase modificada: ", frase_modificada)