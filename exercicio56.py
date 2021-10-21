somaidade = 0
mediaidade = 0
maioridadehomem = 0
totaldemulheres = 0
lista = []
for p in range(1, 5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade = somaidade + idade
    if sexo in 'Mm':
        lista = lista + [idade]
    if sexo in 'Ff' and idade < 20:
        totaldemulheres = totaldemulheres + 1
mediaidade = somaidade / 4
print('A média de idade o grupo é de {} anos'.format(mediaidade))
print('A idade do homem mais velho é {}'.format(max(lista)))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totaldemulheres))
