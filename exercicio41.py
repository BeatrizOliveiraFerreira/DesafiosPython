from datetime import date
ano_de_nascimento = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano_de_nascimento
print('Sua idade é: {}'.format(idade))

if idade <= 9:
    print('Até 9 anos, MIRIM')
elif idade <= 14:
    print('Até 14 anos, INFANTIL')
elif idade <= 19:
    print('Até 19 anos, JUNIOR')
elif idade <= 20:
    print('Até 20 anos, SÊNIOR')
elif idade > 20:
    print('Acima de 20 anos, MASTER')
