while True:
    #Entrada
    num = int(input("Digite um número para ver sua tabuada (digite um número negativo para sair): "))
    #Processamento
    if num < 0:
        break
        
    print(f"Tabuada do {num}:")
    for i in range(1, 11):
        #Saida
        print(f"{num} x {i} = {num*i}")