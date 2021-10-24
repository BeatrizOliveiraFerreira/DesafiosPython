print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Qual o valor a ser sacado? R$'))
total = valor
cedula = 50
totalCedulas = 0
while True:
    if total >= cedula:
        total = total - cedula
        totalCedulas = totalCedulas + 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedulas = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV, tenha um bom dia')

