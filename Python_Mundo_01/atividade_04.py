#Exercício Python 4: 
#Fazendo um programa que lê algo pelo teclado e mostre na tela o seu tipo primitivo e outras informações sobre ele.

a = input('Digite Algo: ')
print('O tipo primitivo do valor digitado é {}'.format(type(a)))
print('É um número?', (a.isnumeric()))
print('É alfabético?', (a.isalpha()))
print('É alfanumérico? ', (a.isalnum()))
print('É somente letras maiúsculas?', (a.isupper()))
print('É somente letras minúsculas?', (a.islower()))
print('Está capitalizada?', (a.istitle()))
print('Tem somente espaços?', (a.isspace()))