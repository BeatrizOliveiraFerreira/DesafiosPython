# Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa
from math import hypot

catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('O comprimento da hipotenusa é = {}{:.2f}{}'.format('\033[31m', hipotenusa, '\033[m'))



