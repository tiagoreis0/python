print('Faca um algoritmo que leia o preco de um produto e mostre seu novo preco com desconto, com 5% de desconto:')
p = float(input('Digite o preco do produto: '))

t = p * 0.05
d = p - t

print('O valor total do desconto é R$ {} '.format(t))
print('O valor do produto com desconto é R$ {}'.format(d))