#Entrada
preco = float(input("Digite o preço do produto: R$ "))
print("Formas de pagamento:")
print("[1] à vista dinheiro/pix")
print("[2] à vista no cartão")
print("[3] em até 2x no cartão")
print("[4] 3x ou mais no cartão")
opcao = int(input("Escolha uma opção: "))

#Processamento
if opcao == 1:
    preco_final = preco * 0.9
elif opcao == 2:
    preco_final = preco * 0.95
elif opcao == 3:
    preco_final = preco
else:
    preco_final = preco * 1.2
    num_parcelas = int(input("Quantas parcelas? "))

#Saida
print(f"Parcelado em {num_parcelas}x de R$ {preco_final/num_parcelas:.2f} (total a pagar: R$ {preco_final:.2f})")