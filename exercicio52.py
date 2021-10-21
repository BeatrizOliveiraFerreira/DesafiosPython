total = 0
numero = int(input('Digite um número: '))
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
if total == 2:
    print('É PRIMO')
else:
    print('\033[31m', 'NÃO É PRIMO')
