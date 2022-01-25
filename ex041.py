'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER
'''
from datetime import date
AnoAtual = date.today().year
AnoNascimento = int(input('Digite seu ano de nascimento: '))

Idade = AnoAtual - AnoNascimento

if Idade <= 9:
    print('Sua idade é {} entao voce é Mirim'.format(Idade))
elif Idade > 9 and Idade <= 14:
    print('Sua idade é {} então voce é INFANTIL'.format(Idade))
elif Idade > 14 and Idade <= 19:
    print('Sua idade é {} entao voce é JUNIOR'.format(Idade))
elif Idade > 19 and Idade <= 25:
    print('Sua idade é {} entao voce é SENIOR'.format(Idade))
else:
    print('Sua idade é {} entao voce é MASTER'.format(Idade))

