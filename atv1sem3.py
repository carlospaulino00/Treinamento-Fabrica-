cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    #Entrada
    num = int(input('Digite um numero entre 0 e 10: '))
    #Processamento
    if 0 <= num <= 10:
        break
    print('Tente novamente. ')
#Saida
print(f'Voce digitou o numero {cont[num]}')