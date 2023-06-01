#Processamento
def voto(ano_nascimento):
    idade = 2023 - ano_nascimento
    
    if idade < 16:
        return "VOTO NEGADO"
    elif (idade >= 16 and idade < 18) or idade >= 70:
        return "VOTO OPCIONAL"
    else:
        return "VOTO OBRIGATÓRIO"
#Entrada
ano = int(input("Digite o ano de nascimento: "))

tipo_voto = voto(ano)

#Saida
print("Tipo de voto:", tipo_voto)
