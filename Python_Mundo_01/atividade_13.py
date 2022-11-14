# Exercício Python 13: 
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o valor do seu salário atual? '))
reajuste = (15*salario) / 100 + salario
print('Trago boas notícias! seu salário terá um reajuste de +15%')
print('A partir de 1/JANEIRO/2023, você receberá > R$ {:.2f}'.format(reajuste))
