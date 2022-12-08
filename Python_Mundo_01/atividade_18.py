# Exercício Python 18: 
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite um Ângulo qualquer: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tag = math.tan(math.radians(ang))
print('O seno do número digitado é {:.4f}'.format(seno))
print('O cosseno do número digitado é {:.4f}'.format(cos))
print('A tangente do número digitado é {:.4f}'.format(tag))