#Processamento
def escreva(texto):
    tamanho = len(texto) + 4
    print("-" * tamanho)
    print(f"  {texto}  ")
    print("-" * tamanho)

#Entrda
texto = input("Digite um texto: ")
#Saida
escreva(texto)
