'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km mostre uma mensagem dizendo que ele foi multador
A multa vai custa R$7.00 por cada KM acima do limite de velocidade'''

velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! voce excedeu o limite de velocidade de 80Km/h ')
    print('Voce deve pagar uma multa de {}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com seguranca.')

