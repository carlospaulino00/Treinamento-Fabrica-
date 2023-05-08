texto = input("Digite uma string: ")#Entrada

contagem = 0
#Processamento
for letra in texto:
    if letra.isalpha():
        contagem += 1

#Saida
print("A string contém", contagem, "letras.")