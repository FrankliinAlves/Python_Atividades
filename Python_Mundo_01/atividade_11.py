#Exercício Python 11: 

'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
print('A área de sua parede equivale a {:.2f}m².'.format(area))
print('Para pintar a sua parede, você deverá comprar {}L de tinta.'.format(area / 2))
