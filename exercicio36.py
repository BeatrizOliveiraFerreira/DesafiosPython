casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o salário do comprador? '))
anos = int(input('Quantos anos de financiamento? '))
prestacao_mensal = casa / (anos * 12)
print('A prestação mensal da casa de {} anos vai ser de {:.2f}'.format(anos, prestacao_mensal))
trinta_por_cento = salario * 30 / 100
if prestacao_mensal <= trinta_por_cento:
    print('\033[32m', 'Empréstimo aprovado', '\033[m')
else:
    print('\033[31m', 'Empréstimo negado, pois excedeu os 30%', '\033[m')
