import random
from time import sleep
'''Crie um programa que faça o computador jogar Jokenpô com você.'''

print('-----PEDRA, PAPEL E TESOURA-----')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

itens = ('Pedra', 'Papel', 'Tesoura')

jogador = int(input('Escolha a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO!!!')
computador = random.randint(0, 2)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATA')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('OPÇAO INVALIDA')
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATA')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('OPÇAO INVALIDA')
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATA')
    else:
        print('OPÇAO INVALIDA')
