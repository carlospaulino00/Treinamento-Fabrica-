lista_pessoas = []

while True:
    #Entrada
    nome = input("Digite o nome da pessoa (ou digite 'sair' para encerrar): ")
    
    #Processamento
    if nome.lower() == 'sair':
        break
    
    peso = float(input("Digite o peso da pessoa: "))

    lista_pessoas.append((nome, peso))

quantidade_pessoas = len(lista_pessoas)

lista_pessoas.sort(key=lambda x: x[1], reverse=True)
pessoas_mais_pesadas = lista_pessoas[:3]  

lista_pessoas.sort(key=lambda x: x[1])
pessoas_mais_leves = lista_pessoas[:3]  

#Saida
print("Quantidade de pessoas cadastradas:", quantidade_pessoas)
print("Pessoas mais pesadas:")
for pessoa in pessoas_mais_pesadas:
    print(f"Nome: {pessoa[0]}, Peso: {pessoa[1]}")
print("Pessoas mais leves:")
for pessoa in pessoas_mais_leves:
    print(f"Nome: {pessoa[0]}, Peso: {pessoa[1]}")
