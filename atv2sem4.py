#Processamento
def área(largura, comprimento):
    area = largura * comprimento
    return area
#Entrada
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))

resultado = área(largura, comprimento)
#Saida
print("A área do terreno é:", resultado)
