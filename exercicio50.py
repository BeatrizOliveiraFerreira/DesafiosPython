soma = 0
count = 0
for i in range(1, 7):
    valor = int(input('Digite um valor: '))
    if i % 2 == 0:
        soma = soma + valor
        count = count + 1
print('A soma de todos os {} números PARES é igual a {}'.format(count, soma))


