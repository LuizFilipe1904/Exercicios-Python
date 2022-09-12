'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

from cmath import inf


numeros = []

maiorNumero = -inf
menorNumero = inf
soma = 0

while True:
    n = input("Digite um número. Quando quiser parar digite 'stop': ")
    if n.lower() == 'stop':
        break
    numeros.append(int(n))


for numero in numeros:
    if (numero > maiorNumero):
        maiorNumero = numero
print(f"O maior número é {maiorNumero}")

for numero in numeros:
    if (numero < menorNumero):
        menorNumero = numero
print(f"O menor número é {menorNumero}")

for numero in numeros:
    soma += numero
print(f"A soma dos números é de {soma}")