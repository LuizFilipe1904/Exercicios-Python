'''
Faça um programa que leia um número n e crie um vetor que armazena os valores dos fatoriais de 0 até n e imprima no final
'''
n = int(input('Digite até qual número deseja calcular: '))
fats = []
fat = 1

for i in range(2, n + 1):
    fat *= i
    fats.append(fat)

print(fats)