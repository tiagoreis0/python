print('Faca um programa que leia a altura e largura de uma parede em metros'
      'calcule sua area e quantidade de tinta necessaria para pinta-la, sabendo que'
      'cada litro de tinta printa uma area de 2M')

a = float(input('Digite altura da parede: '))
l = float(input('Digite a largura da parede: '))

total = a * l

tinta = total / 2
print('O tatol de metros quadrado da parede é {} '.format(total))
print('O A quantidade de tinta necessaria para print a area {} metros e de {} litros '.format(total, tinta))
