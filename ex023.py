print('Faca um programa que leia um numero de 0 a 9999 e mostre na tela os numeros separados0')

numero = int(input('Digite um numero: '))

n = str(numero)

print('Unidade {}'.format(n[3]))
print('Dezena {}'.format(n[2]))
print('Cetena {}'.format(n[1]))
print('Milhar {}'.format(n[0]))
