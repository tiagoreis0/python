print('Escreva um programa que leia um valor em metros e o exiba em convertido em centimetros e milimeros:')

metros = float(input('Digite um numero: '))

c = metros * 100
m = metros * 1000

print('O numero {} convertido fica {} centimetros'.format(metros, c))
print('O numero {} convertido fica {} milimitros'.format(metros, m))
