'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

notas = []
soma = 0

for i in range(4):
    nota = float(input('Digite as 4 notas: '))
    while nota < 0:
        nota = float(
            input('Notas negativas não são válidas, digite novamente: '))
    notas.append(nota)
    soma += nota

print(f'As notas foram: {notas}')

media = soma / 4
print(f'A média dessas notas foram: {media}')
