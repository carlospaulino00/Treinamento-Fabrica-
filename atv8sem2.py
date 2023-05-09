
while True:
    print("[1] SOMA")
    print("[2] MULTIPLICAR")
    print("[3] MAIOR")
    print("[4] NOVOS NÚMEROS")
    print("[5] SAIR DO PROGRAMA")

    #Entrada
    opcao = int(input("Escolha uma opção: "))

    #Processamento
    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        #Saida
        print(f"A soma entre {num1} e {num2} é {resultado:.2f}")
    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"A multiplicação entre {num1} e {num2} é {resultado:.2f}")
    elif opcao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num1 > num2:
            resultado = num1
        else:
            resultado = num2
        print(f"O maior número entre {num1} e {num2} é {resultado:.2f}")
    elif opcao == 4:

        continue
    elif opcao == 5:

        break
    else:
        print("Opção inválida. Tente novamente.")