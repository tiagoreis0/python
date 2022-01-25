'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
'''

peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual e o sua altura: '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print('O IMC dessa pessoa é {:.2f}'.format(imc))
    print('VOCE ESTA ABAIXO DO PESO')
elif imc <= 25:
    print('O IMC dessa pessoa é {:.2f}'.format(imc))
    print('PESO IDEAL')
elif imc <= 30:
    print('O IMC dessa pessoa é {:.2f}'.format(imc))
    print('SOBREPESO')
elif imc <= 40:
    print('O IMC dessa pessoa é {:.2f}'.format(imc))
    print('OBESIDADE')
else:
    print('O IMC dessa pessoa é {:.2f}'.format(imc))
    print('OBESIDADE MORBIDA')
