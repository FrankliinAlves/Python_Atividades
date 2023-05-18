# Exercício Python 24: 
#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “RIO”.

cidade = str(input('Digite o nome da cidade: ')).strip().upper()

if "RIO" in  cidade[:3]:
    print("O nome da cidade digitado começa com a palavra RIO.")
else:
    print("O nome da cidade digitado NÃO começa a palavra RIO.")