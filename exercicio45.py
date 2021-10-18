from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')
jogador = int(input('Escolha uma das opções: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 20)
print('O computador jogou {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[jogador]))
print('-=' * 20)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('\033[32m', 'VOCÊ VENCEU!!')
    elif jogador == 2:
        print('\033[31m', 'O COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('\033[31m', 'O COMPUTADOR VENCEU')
    elif jogador == 1:
        print('\033[35m', 'EMPATE')
    elif jogador == 2:
        print('\033[32m', 'VOCÊ VENCEU!!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('\033[32m', 'VOCÊ VENCEU')
    elif jogador == 1:
        print('\033[31m', 'O COMPUTADOR VENCE')
    elif jogador == 2:
        print('\033[35m', 'EMPATE')
    else:
        print('JOGADA INVÁLIDA')
