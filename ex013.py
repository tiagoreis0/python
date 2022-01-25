print('Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario  com 15% de aumento: ')

s = float(input('Digite seu salario: '))

t = (s * 15) / 100 + s
print('O seu novo salario com 15% aumento é R$ {:.2f} '.format(t))
