numero = list()
while True:
    number = int(input('Digite um valor: '))
    if number not in numero:
        numero.append(number)
    else:
        print('Valor duplicado, não vou adicionar')

    quer_continuar = str(input('Quer continuar? [S/N] -> ')).strip().upper()[0]
    if quer_continuar == 'N':
        break
print(f'Os números colocados foram: {sorted(numero)}')


