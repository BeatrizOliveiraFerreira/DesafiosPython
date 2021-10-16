# O mesmo professor do desafio anterior quer sortear
# a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre
# a ordem sorteada
import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terçeiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
ordemApresentacao = listaAlunos
random.shuffle(ordemApresentacao)
print('A ordem de apresentação é: {}{}{}'.format('\033[1;44m', ordemApresentacao, '\033[m'))



