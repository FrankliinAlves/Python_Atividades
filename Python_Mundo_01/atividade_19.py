# Exercício Python 19: 
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
dig1 = str(input('Digite o nome do 1° aluno: '))
dig2 = str(input('Digite o nome do 2° aluno: '))
dig3 = str(input('Digite o nome do 3° aluno: '))
dig4 = str(input('Digite o nome do 4° aluno: '))

nomes = [dig1, dig2, dig3, dig4]
escolhido = random.choice(nomes)

print('O aluno(a) sorteado(a) para fazer a leitura do texto foi {}.'.format(escolhido))