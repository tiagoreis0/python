'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Digite seu salario: '))

if salario > 1250:
    aumento = (salario * 0.10) + salario
    print('Quem ganhava R${:.2f} passa a ganha R${:.2f}'.format(salario, aumento))
else:
    aumento = (salario * 0.15) + salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, aumento))
