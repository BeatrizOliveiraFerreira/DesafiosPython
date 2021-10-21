from datetime import date
atual = date.today().year
maior_de_idade = 0
menor_de_idade = 0
for i in range(1, 8):
    nascimento = int(input('Em que ano essa pessoa nasceu?'))
    idade = atual - nascimento
    if idade >= 21:
        maior_de_idade = maior_de_idade + 1
    else:
        menor_de_idade = menor_de_idade + 1
print('São {} pessoas maiores de idade'.format(maior_de_idade))
print('São {} pessoas menores de idade'.format(menor_de_idade))

