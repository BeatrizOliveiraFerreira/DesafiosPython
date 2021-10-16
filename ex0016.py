# Um professor quer sortear um dos quatro alunos
# para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
alunos = [nome1, nome2, nome3, nome4]
alunoEscolhido = choice(alunos)
print('O aluno sorteado é: {}{}{}'.format('\033[31m', alunoEscolhido, '\033[m'))





















