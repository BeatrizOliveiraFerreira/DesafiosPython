numero = int(input('Digite o número: '))
razao = int(input('Digite a razão: '))
decimo = numero + (11 - 1) * razao
for i in range(numero, decimo, razao):
    print('{} '.format(i), end='-> ')
print('ACABOU!!')
