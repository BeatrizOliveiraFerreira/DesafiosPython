# Crie uma lista onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')

# valor = list()
# par = impar = 0
# for c in range(0, 7):
#     valor.append(int(input('Digite um valor: ')))
#     valor.sort()
#
# for v in valor:
#     if v % 2 == 0:
#         par += 1
#     else:
#         impar += 1
#
# print(f'Foi um total de {par} valores pares')
# print(f'Foi um total de {impar} valores ímpares')


