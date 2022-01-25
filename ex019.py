import random
print('Um professor quer sortear um dos seus quatros alunos para apagar o quadro .')
print('Faca um programa que ajude ele, lendo o nome deles e escreva o nome escolhido')

n1 = input('Digite seu nome:')
n2 = input('Digite seu nome:')
n3 = input('Digite seu nome:')
n4 = input('Digite seu nome:')

lista = [n1, n2, n3, n4]

sorteio = random.choice(lista)

print('O aluno escolhido é {} '.format(sorteio))

