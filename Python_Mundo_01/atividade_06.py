#Exercício Python 6: 
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número: '))
raiz = float(n) ** 0.5
print('O dobro do número digitado é = {:.0f}\nO triplo do número digitado é = {:.0f}\n'
      'A raiz quadrada do número digitado é = {:.2f}'.format(n*2, n*3, raiz))