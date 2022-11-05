#Exercício Python 10:
#Crie um programa que leia quanto dinheiro uma pessoa tem em sua carteira Brasileira e converta para dólares.
# >>> conversor básico com atualização manual da cotação do dolar.

real = float(input('Quanto você tem na carteira Brasileira? R$ '))
dolar = real / 5.04
print('A cotação do dolar no dia 05/11/2022 = US$ 5.04')
print('Com esse valor de R${:.2f}, você teria no EUA US$ {:.2f}'.format(real,dolar))