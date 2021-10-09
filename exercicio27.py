name = str(input('Digite o seu nome: ')).strip()
print('Muito prazer em te conhecer {} !'.format(name))
nome = name.split()
print('O seu primeiro nome é: {}'.format(nome[0]))
print('O seu último nome é: {}'.format(nome[len(nome) - 1]))


