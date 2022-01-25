print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ele pode comprar')

d = float(input('Quanto dinheiro voce tem: '))

t = d / 5.19

print('Voce tem R$ {:.2f} da para comprar $ {:.2f} '.format(d, t))
