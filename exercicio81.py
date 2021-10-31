numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] -> ')).strip().upper()[0]
    if r == 'N':
        break

print(f'Foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f'Em ordem decrescente ficou {numeros}')

if 5 in numeros:
    print('O número 5 está na lista!')
else:
    print('O número 5 NÃO está na lista!')








