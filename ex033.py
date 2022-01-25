'''Faca um progama que leia 3 numeros e mostre qual e o maior e qual e o menor'''

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite mais um numero: '))

menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#testando o maior
maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O mairo numero digitado foi {}'.format(maior))
print('Menor numero digitado doi {}'.format(menor))
