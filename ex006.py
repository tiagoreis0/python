print('Crie um algoritimo que leia um numero e mostre seu dobro, tripo e raiz quadrada:')

n = int(input('Digite um numero: '))

dobro = n * 2
triplo = n * 6
raiz = n**(1/2)

print('O dobro de {} é {}'.format(n, dobro))
print('O triplo de {} e {} '.format(n, triplo))
print('A raiz quadrada de {} é {:.2f} '.format(n, raiz))
