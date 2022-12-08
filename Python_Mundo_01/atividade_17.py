# Exercício Python 17: 
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

# Solução 01
catop = float(input('Qual a medida do cateto oposto? '))
catadj = float(input('Qual a medida do cateto adjacente? '))
hip = (catop ** 2 + catadj ** 2) ** (1/2)
print('A hipotenusa dos catetos digitados é = {:.2f}'.format(hip))

# solução 02
from math import hypot
catop = float(input('Digite o cat oposto: '))
catadj = float(input('Digite o cat adjacente: '))
hip = hypot(catop, catadj)
print('A hipotenusa dos catetos digitados é {:.2f}'.format(hip))