#Entrada
palavras = ("python", "pedro", "treinamento", "carro", "arroz")

#Processamento  
vogais = "aeiou"

for palavra in palavras:
    vogais_palavra = [letra for letra in palavra if letra.lower() in vogais]
    #Saida
    print(f"Vogais em '{palavra}': {', '.join(vogais_palavra)}")