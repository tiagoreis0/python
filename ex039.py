'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
atual = date.today().year

Ano = int(input('Digite sua data de nascimento: '))
genero = str(input('Homem ou Mulher: '))

idade = atual - Ano
print('Quem nasceu em {} tem {} anos em {}'.format(Ano, idade, atual))
if genero == 'Homem':
    if idade == 18:
        print('Voce tem que se alista IMEDIATAMENTE')
    elif idade < 18:
        saldo = 18 - idade
        anolist = saldo + atual
        print('Ainda falta {} anos para o alistamento'.format(saldo))
        print('Seu alistamento sera {} '.format(anolist))
    else:
        saldo = idade - 18
        anolist = atual - saldo
        print('Voce ja deveria ter se alistado há {}'.format(saldo))
        print('Seu alistamento foi em {}'.format(anolist))
else:
    print('Voce é mulher, nao precisa se alistar')