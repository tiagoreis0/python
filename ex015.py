print('Escreva um programa que pergunte a quantidade de Km percorridos \n por um carro alugado e a quantidade de'
      ' dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo \n que o carro custa R$60 por dia e R$0,15'
      ' por Km rodado')

k = float(input('Quantos KM percorridos: '))
d = int(input('Quantos dias ele foi alugado: '))

t = (k * 0.15) + (d * 60)

print('O total a pagar é R${}'.format(t))
