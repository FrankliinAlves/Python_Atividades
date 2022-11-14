# Exercício Python 15: 
""" Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. """

dias_alugado = int(input('Informe a quantidade de dias locado: '))
km_percorrido = float(input('Informe a quilometragem rodada: '))
dia_locado = dias_alugado * 60
preco_km = km_percorrido * 0.15
print('Custo a pagar por dias locado = R$ {:.2f}'.format(dia_locado))
print('Custo a pagar por km rodado = R$ {:.2f}'.format(preco_km))
print('Valor total a pagar = R$ {:.2f}'.format(dia_locado + preco_km))



