'''Digite um numero e diga se ele e impa ou par'''

numero = int(input('Digite um numero'))

resultado = numero % 2

if resultado == 0:
    print('O numero digitado {} é PAR '.format(numero))
else:
    print('O numero digitado {} é impar '.format(numero))

