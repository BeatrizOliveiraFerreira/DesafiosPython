print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro número: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razão
    cont = cont + 1
print('FIM!!')