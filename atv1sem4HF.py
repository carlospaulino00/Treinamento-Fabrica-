#Processamento
def contador(inicio, fim, passo):
    #Saida
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")
    
    if passo > 0:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ")
    else:
        for i in range(inicio, fim - 1, passo):
            print(i, end=" ")
    
    print("\n")

#Entrada
contador(1, 10, 1)

contador(10, 0, -2)

contador(3, 15, 4)
