'''Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao'''

Numero = int(input('Digite um numero: '))
print('''
[1] converter para BINARIO
[2] converter para OCTA
[3] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINARIO é {}'.format(Numero, bin(Numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(Numero, oct(Numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL {}'.format(Numero, hex(Numero)[2:]))
else:
    print('Opção invalida')

