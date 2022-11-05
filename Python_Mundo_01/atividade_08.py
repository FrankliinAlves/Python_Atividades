#Exercício Python 8: 
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite a medida em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida digitada convertida em centimetros é = {:.0f} cm\n'
      'A medida digitada convertida em milímetros é = {:.0f} mm'.format(cm, mm))
      