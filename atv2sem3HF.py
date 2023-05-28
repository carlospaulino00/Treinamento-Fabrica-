#Entrada
produtos = (
    ("Camiseta", 29.90),
    ("Calça jeans", 99.90),
    ("Tênis", 149.90),
    ("Meias", 9.90),
    ("Boné", 19.90)
)

# #Saida
print("PRODUTOS\t\tPREÇOS")

for produto, preco in produtos:
    print(f"{produto: <15}\tR${preco:.2f}")

