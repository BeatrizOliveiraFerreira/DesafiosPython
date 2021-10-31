# Faça um programa que leia o nome e peso de várias pessoas, [ X ]
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas [ X ]
# B) Uma lista com as pessoas mais pesadas, [ X ]
# C) Uma lista com as pessoas mais leves [ X ]

temporal = list()
principal = list()
leve = pesado = 0
while True:
    temporal.append(str(input('Nome: ')))
    temporal.append(float(input('Peso: ')))
    if len(principal) == 0:
        leve = pesado = temporal[1]
    else:
        if temporal[1] > pesado:
            pesado = temporal[1]
        if temporal[1] < leve:
            leve = temporal[1]
    principal.append(temporal[:])
    temporal.clear()
    continuar = str(input('Quer continuar? [S/N] -> ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Os dados foram {principal}')
print(f'Ao todo você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {pesado}Kg. Peso de ', end='')
for p in principal:
    if p[1] == pesado:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {leve}Kg. Peso de ', end='')
for p in principal:
    if p[1] == leve:
        print(f'[{p[0]}] ', end='')
print()
















