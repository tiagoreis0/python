'''print('faca um programa que leia o cateto oposto e do cateto adjacente de um triangulo retangulo')
print('calcule e mostre o comprimento da hipotenusa')

co = float(input('Digite o cateto oposto: '))
ca = float(input('digite o comprimento adjacente: '))

hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f} '.format(hi))'''

import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('digite o comprimento adjacente: '))
hi = (math.hypot(co, ca))

print('A hipotenusa vai medir {:.2f} '.format(hi))