'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''

numeros = []
pares = []
impares = []

for i in range(20):
    n = int(input('Digite um número: '))
    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Os números digitados foram: {numeros}')
print(f'Os números pares foram: {pares}')
print(f'Os números impares foram: {impares}')
