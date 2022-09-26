'''
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''

alturas = []
inf = []

for i in range(30):
    print(f'Aluno {i + 1}')
    idade = int(input('Informe a idade do aluno: '))
    alt = float(input('Informe a altura do aluno: '))
    alturas.append(alt)

soma = sum(alturas)
media = soma / len(alturas)

if idade > 13 and alt < media:
    inf.append(alt)
print(len(inf))
