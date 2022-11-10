# Exercício Python 12: 
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual o valor do produto? '))
desc = 5 * produto / 100
print('Com um desconto de 5%, o seu produto custará apenas {:.2f}R$'.format(produto - desc))