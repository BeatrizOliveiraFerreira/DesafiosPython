name = str(input('Digite o seu nome: ')).strip()
print('Muito prazer em te conhecer {}{}{} !'.format('\033[31m', name, '\033[m'))
nome = name.split()
print('O seu primeiro nome é: {}{}{}'.format('\033[33m', nome[0], '\033[m'))
print('O seu último nome é: {}'.format(nome[len(nome) - 1]))





