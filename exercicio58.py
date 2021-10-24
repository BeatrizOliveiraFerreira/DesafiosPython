from random import randint
computador = randint(0, 10)
print('Sou o seu computador e pensei em um número...')
print('Você consegue adivinhar em qual número eu pensei?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente')
        elif jogador > computador:
            print('Menos... Tente novamente')
print('Acertou com {} tentativas, parabéns!!'.format(palpites))
