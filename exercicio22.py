nome = str(input('Digite o seu nome: ')).strip()
print('Nome em Maiúsculo: {}'.format(nome.upper()))
print('Nome em Minúsculo: {}'.format(nome.lower()))
print('Nome total: {}'.format(len(nome) - nome.count(' ')))
nome_com_split = nome.split()
print('O primeiro nome tem {} letras'.format(len(nome_com_split[0])))








