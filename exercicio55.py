lista = []
for c in range(1, 6):
    peso = float(input('Qual o peso da {} pessoa? '.format(c)))
    lista = lista + [peso]
print('O maior peso foi de {}'.format(max(lista)))
print('O menor peso foi de {}'.format(min(lista)))
