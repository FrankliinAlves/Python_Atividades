# Exercício Python 14: 
# Escreva um programa que leia uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Informe a temperatura em Graus Celsius: '))
fahrenheit = ((9*temp)/5)+32
print('A temperatura de {}°C convertida para fahrenheit é {}°F'.format(temp,fahrenheit))
