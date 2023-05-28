# Função para calcular a média das notas de um aluno
def calcular_media(notas):
    return sum(notas) / len(notas)

lista_alunos = []

while True:
    #Entrada
    nome = input("Digite o nome do aluno (ou digite 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        break
    
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    #Processamento
    aluno = [nome, [nota1, nota2]]
    lista_alunos.append(aluno)

print("Boletim:")
for aluno in lista_alunos:
    nome = aluno[0]
    notas = aluno[1]
    media = calcular_media(notas)
    print(f"Aluno: {nome} - Média: {media:.2f}")

while True:
    opcao = input("Digite o nome do aluno para ver as notas (ou digite 'sair' para encerrar): ")

    if opcao.lower() == 'sair':
        break

    encontrado = False
    #Saida
    for aluno in lista_alunos:
        nome = aluno[0]
        notas = aluno[1]
        if nome.lower() == opcao.lower():
            encontrado = True
            print(f"Notas do aluno {nome}: {notas}")
            break
    
    if not encontrado:
        print("Aluno não encontrado.")
