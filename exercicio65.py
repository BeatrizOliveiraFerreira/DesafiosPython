resp = 'S'
soma = quantidade_de_numeros = media = maior = menor = 0
while resp in 'Ss':
    numero = int(input('Digite um número: '))
    soma = soma + numero
    quantidade_de_numeros = quantidade_de_numeros + 1
    if quantidade_de_numeros == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / quantidade_de_numeros
print('Você digitou {} números e a média foi {}'.format(quantidade_de_numeros, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))


