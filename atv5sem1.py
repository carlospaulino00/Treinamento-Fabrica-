distancia_km = float(input("Digite a distância em km: "))#Entrada

#Processamento
if distancia_km <= 200:
    preco_passagem = distancia_km * 1.5
else:
    preco_passagem = distancia_km * 1.25

print(f"O preço da passagem é: R${preco_passagem:.2f}")#Saida