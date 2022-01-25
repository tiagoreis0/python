#import math
from math import trunc
print('cire um programa que leia um numero real qualquer que leia \n pelo teclado e  '
      'mostre na tela sua porção inteira')

n = float(input('Digite um numero: '))

# i = math.trunc(n)
i = trunc(n)


print('O numero {} tem a parte inteira {}'.format(n, i))
