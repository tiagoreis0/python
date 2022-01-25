''' sccreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
    - O primeiro valor é maior
    - O segundo valor é maior
    - Não existe valor maior, os dois são iguais '''

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

if numero1 > numero2:
    print('O PRIMEIRO numero é maior')
elif numero2 > numero1:
    print('O SEGUNDO numero é maior')
else:
    print('O PRIMEIRO e SEGUNDO numero são IGUAIS')
