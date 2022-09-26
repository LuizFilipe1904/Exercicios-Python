'''
Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''

media = 0
soma = 0
medias = []
mediasMaiores = []

for i in range(10):
    print(f'Aluno {i + 1}')

    for j in range(4):
        nota = float(input('Digite as 4 notas: '))
        while nota < 0 or nota > 10:
            nota = float(input('Nota inválida, digite novamente: '))
        soma += nota

    media = soma / 4
    if media >= 7:
        mediasMaiores.append(media)
    else:
        medias.append(media)

print(f'Foram {len(mediasMaiores)} alunos com medias maiores ou iguais a 7.')