#Processamento
def ficha(nome='', gols=0):
    if nome.strip() == '':
        nome = 'desconhecido'
    if not gols.isnumeric():
        gols = 0
    
    print(f"Jogador: {nome}")
    print(f"Gols marcados: {gols}")

#Entrada
nome = input("Digite o nome do jogador: ")
gols = input("Digite a quantidade de gols: ")

#Saida 
ficha(nome, gols)
