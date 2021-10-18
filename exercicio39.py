from datetime import date
atual = date.today().year
nascimento = int(input('Qual é o seu ano de nascimento? '))
idade = atual - nascimento
print('Você tem {} anos de idade'.format(idade))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE')
elif idade > 18:
    deveria = idade - 18
    ano_de_alistamento = atual - deveria
    print('Você já deveria ter se alistado a {} anos'.format(deveria))
    print('Deveria ter se alistado no ano de {}'.format(ano_de_alistamento))
elif idade < 18:
    faltam = 18 - idade
    ano_que_vai_se_alistar = atual + faltam
    print('Faltam {} anos para você se alistar'.format(faltam))
    print('Você deve se alistar no ano {}'.format(ano_que_vai_se_alistar))

