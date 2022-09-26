'''
Escreva um programa que leia uma lista de 10 elementos numéricos e imprima o valor da soma e a média desses valores
sem usar a função sum()
'''

nums = []
soma = 0

for i in range(10):
    num = int(input('Digite um número: '))
    nums.append(num)
    soma += num

media = soma / len(nums)

print(f'A soma dos valores é de: {soma}')
print(f'A média dos valores é de: {media}')