nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi: {}'.format(media))
if media < 5:
    print('REPROVADO!')
elif 5 <= media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')
