#Processamento
def encontrar_maior(*args):
    maior_valor = float('0')  
    
    for valor in args:
        if valor > maior_valor:
            maior_valor = valor
    
    return maior_valor
#Entrada
valores = input("Digite os valores separados por espaço: ")
valores_inteiros = [int(valor) for valor in valores.split()]

resultado = encontrar_maior(*valores_inteiros)

#Saida
print("O maior valor digitado é:", resultado)

