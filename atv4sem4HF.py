#Processamento
def notar():
    notas = []
    continuar = True

    while continuar:
        #Entrada
        nota = float(input("Digite a nota do aluno: "))
        notas.append(nota)

        resposta = input("Deseja continuar digitando notas? (S/N) ")
        if resposta.upper() != "S":
            continuar = False

    quantidade = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / quantidade

    informacoes = {
        'Quantidade de notas': quantidade,
        'Maior nota': maior,
        'Menor nota': menor,
        'Média da turma': media
    }

    return informacoes

resultado = notar()
#Saida
for chave, valor in resultado.items():
    print(f'{chave}: {valor}')
