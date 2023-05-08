#Exercício Python 22: 
#Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome = input(str("digite o nome: "))
tamanho = len(nome)
print("O nome digitado em maiúsculo = {}.".format(nome.upper()))
print("O nome digitado em minúsculo = {}.".format(nome.lower()))
print("O tamanho do nome digitado =", tamanho, 'letras.')
print("O primeiro nome tem {} letras.".format(nome.find(' ')))
