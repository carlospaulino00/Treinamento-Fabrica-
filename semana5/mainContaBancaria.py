from contaBancaria import ContaBancaria

conta1 = ContaBancaria("João", "123456", 1000.0)

opcao = input("Digite 'D' para depositar, 'S' para sacar ou 'V' para verificar o saldo: ")

if opcao == "D":
    valor = float(input("Digite o valor a ser depositado: "))
    conta1.depositar(valor)
elif opcao == "S":
    valor = float(input("Digite o valor a ser sacado: "))
    conta1.sacar(valor)
elif opcao == "V":
    conta1.verificar_saldo()
else:
    print("Opção inválida.")
