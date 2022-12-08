# Exercício Python 20: 
# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
dig1 = str(input('Digite o 1° aluno: '))
dig2 = str(input('Digite o 2° aluno: '))
dig3 = str(input('Digite o 3° aluno: '))
dig4 = str(input('Digite o 4° aluno: '))

nomes = [dig1, dig2, dig3, dig4]
shuffle(nomes)

print('A ordem de apresentação será {}'.format(nomes))
