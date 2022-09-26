'''
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

A = []
quads = []

for i in range(10):
    print(f'Número {i + 1}')
    num = int(input('Digite um número: '))
    A.append(num)

for num in A:
    quad = num ** 2
    quads.append(quad)

soma = sum(quads)
print(f'A soma dos quadrados é de: {soma}')