# Exercício Python 25: 
# Crie um programa que leia o nome de uma pessoa e diga se o nome digitado tem a palavra  “SILVA”.

nome = str(input('Digite seu nome: ')).strip().upper()

if 'SILVA' in nome:
    print('O nome digitado tem SILVA.')
else:
    print('O nome digitado não tem SILVA.')
