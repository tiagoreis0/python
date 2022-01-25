'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
'''

Nota1 = float(input("DIGITE A PRIMEIRA NOTA: "))
Nota2 = float(input("DIGITE A SEGUNDA NOTA: "))

Media = (Nota1 + Nota2) / 2

if Media < 5:
    print('Tirando {} e {} a media é {}'.format(Nota1, Nota2, Media))
    print('VOCE ESTA APROVADO')
elif Media >= 5.0 and Media <= 6.9:
    print('Tirando {} e {} a media é {}'.format(Nota1, Nota2, Media))
    print('VOCE ESTA DE RECUPERAÇÃO')
else:
    print('Tirando {} e {} a media é {}'.format(Nota1, Nota2, Media))
    print('VOCE ESTA APROVADO')