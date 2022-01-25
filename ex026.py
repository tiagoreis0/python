frase = str(input('Digite uma frase: ')).upper().strip()

print('Quantas vezes aparece a letra A: {}'.format(frase.count('A')))
print('Em que posição ela aparece a primeira vez {}'.format(frase.find('A')))
print('Em que posição ela aparece a ultima vez {}'.format(frase.rfind('A')))

