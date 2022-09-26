'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''

mult = 1
numeros = []

for i in range(5):
    print(f'Número {i + 1}')
    num = int(input('Digite um número: '))
    numeros.append(num)
    
for num in numeros:
    mult *= num

print(f'Os números digitados foram: {numeros}')
print(f'A soma dos número é {sum(numeros)}.')
print(f'A multiplicação dos números é de: {mult}')