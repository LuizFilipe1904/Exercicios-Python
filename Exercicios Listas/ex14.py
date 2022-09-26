'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a."Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''

print('Responda as perguntas a seguir com (s) para sim ou (n) para não.')

respostas = []
positivas = []
negativas = []

a = input('Telefonou para vítima? ')
a = a.lower()
respostas.append(a)

b = input('Esteve no local do crime? ')
b = b.lower()
respostas.append(b)

c = input('Mora perto da vítima? ')
c = c.lower()
respostas.append(c)

d = input('Devia para a vítima? ')
d = d.lower()
respostas.append(d)

e = input('Já trabalhou com a vítima? ')
e = e.lower()
respostas.append(e)

for i in respostas:
    if i == 's':
        positivas.append(i)
    else:
        negativas.append(i)

if len(positivas) == 2:
    print('Suspeito')

elif len(positivas) > 2 and len(positivas) <= 4:
    print('Cúmplice')

elif len(positivas) == 5:
    print('Assassino')

else:
    print('Inocente')
