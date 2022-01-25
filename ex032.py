'''faca um programa que leia um ano qualquer e diga se ele bissexto'''
from datetime import datetime
ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year
if ano % 5 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano e Bissexto {}'.format(ano))
else:
    print('O ano nao e bissexto '.format(ano))
