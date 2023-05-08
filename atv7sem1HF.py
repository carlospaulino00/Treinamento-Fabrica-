frase = input("Digite uma frase: ")#Entrada

#Processamento
frase_sem_espacos = frase.replace(" ", "")
tamanho = len(frase_sem_espacos)

#Saida
print("Frase digitada:", frase)
print("Quantidade de caracteres: ", tamanho)