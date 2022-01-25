import math

angulo = float(input('Digite o numero que deseja: '))

seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f} '.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f} '.format(angulo, cosseno))
tangent = math.tan(math.radians(angulo))
print('O angulo de {} tem o TANGENT de {:.2f} '.format(angulo, tangent))