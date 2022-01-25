print('Crie um programa que leia o nome de uma cidade e diga se ela comceca ou nao com o nome SANTOS')

cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()


print(cidade[0:6].upper() == 'SANTOS')

