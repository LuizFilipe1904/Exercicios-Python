'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

lst = []

for i in range(10):
    num = float(input('Digite um número: '))
    lst.append(num)

lst.reverse()
print(lst)
