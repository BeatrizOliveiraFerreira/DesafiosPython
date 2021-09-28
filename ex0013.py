# Crie um programa que leia um numero Real
# qualquer pelo teclado e mostre na tela a sua parte inteira

from math import trunc
numero = float(input('Digite um número Real: '))
print('O número em sua parte inteira é = {}'.format(trunc(numero)))
