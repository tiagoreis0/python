'''escreva um programa que faca o computador pensar em numero de 0 a 5 e
peca ao usuario tentar adivinhar qual numero escolhido pelo usuario'''
import random
numero = int(input('Digite um numero de 0 a 5: '))

aleatorio = random.randint(0, 5)

if numero == aleatorio:
    print('Parabens! Voce digitou o numero {} e numero pensado pelo computador foi {}'.format(numero, aleatorio))
else:
    print('Voce digitou {} e numero escolhido pelo computador foi {}'.format(numero, aleatorio))
