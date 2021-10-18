numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
if numero1 > numero2:
    print('{} é maior'.format(numero1))
elif numero2 > numero1:
    print('{} é maior'.format(numero2))
elif numero1 == numero2:
    print('Não existe valor maior, porque os dois são iguais')