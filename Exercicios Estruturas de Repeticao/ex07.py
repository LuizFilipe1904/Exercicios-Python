'''
Faça um programa que leia 5 números e informe o maior número.
'''

from cmath import inf


numeros = []

for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

maiorNumero = -inf

for numero in numeros:
    if (numero > maiorNumero):
        maiorNumero = numero
    
print(f'O maior número é {maiorNumero}')
