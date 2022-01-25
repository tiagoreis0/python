'''Desenvolva um programa que pergunte a distancia de uma viagem em Km.
   Calcule o preco da passagem , cobrando R$0,50 por km para viagens de ate 200 km
    e R$0,45 para viagens mais longas'''

km = int(input('Quantos km ate o seu destino: '))
print('Voce esta preste a viajar {} km'.format(km))

if km <= 200:
    total = km * 0.50
    print('E o preco da sua passagem sera R${:.2f}'.format(total))
else:
    total = km * 0.45
    print('E o preco da sua passagem sera R${:.2f}'.format(total))
