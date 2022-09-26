'''
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores.
'''

import random


l1 = []
l2 = []
l3 = []

for i in range(10):
    l1.append(random.randint(1, 100))
    l2.append(random.randint(1, 100))
    l3.append(l1[i])
    l3.append(l2[i])

print(l3)
