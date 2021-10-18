comprimento1 = float(input('Qual é o comprimento da primeira reta? '))
comprimento2 = float(input('Qual é o comprimento da segunda reta? '))
comprimento3 = float(input('Qual é o comprimento da terceira reta? '))
if comprimento1 < (comprimento2 + comprimento3) and comprimento2 < (comprimento1 + comprimento3) and comprimento3 < (comprimento1 + comprimento2):
    print('\033[1;45m', 'Podem formar um triângulo', '\033[m', end='')
    if comprimento1 == comprimento2 == comprimento3:
        print('EQUILÁTERO')
    elif comprimento1 != comprimento2 != comprimento3 != comprimento1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('\033[31m', 'Não podem formar um triângulo', '\033[m')

