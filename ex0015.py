# Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, cosseno e a tangente desse
# angulo
from math import radians, sin, cos, tan

numero = float(input('Digite um ângulo: '))
seno = sin(radians(numero))
cosseno = cos(radians(numero))
tangente = tan(radians(numero))

print('O ângulo {}{} é seno {:.2f}, cosseno {:.2f} e tangente {:.2f}{}'.format('\033[43m', numero, seno, cosseno, tangente, '\033[m'))

