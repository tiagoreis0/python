import random

a1 = input('digite um nome: ')
a2 = input('digite um nome: ')
a3 = input('digite um nome: ')
a4 = input('digite um nome: ')

list = [a1, a2, a3, a4]

random.shuffle(list)
print(list)
