num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A de de ímpares é {impares}')



