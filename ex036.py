'''Escreva um programa bancario para a compra de uma casa. O programa vai perguntar o valor da casa
o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo
sera negado'''

ValorDaCasa = float(input('Digite o valor da casa que vc deseja comprar R$: '))
Salario = float(input('Digite o salario da pessoa que quer comprar a casa R$: '))
Ano = int(input('Informe em quantos anos vc quer pagar a casa: '))

PrestacaoDaCasa = ValorDaCasa / (Ano * 12)
Minimo = Salario * 30 / 100

print('Para pagar a casa de RS$ {:.2f} em {} anos sera de R${:.2f} reais'.format(ValorDaCasa, Ano, PrestacaoDaCasa))
if (PrestacaoDaCasa <= Minimo):
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')
