'''
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

import random

l1 = []
l2 = []
l3 = []
l4 = []

for i in range(10):
    l1.append(random.randint(1, 100))
    l2.append(random.randint(1, 100))
    l3.append(random.randint(1, 100))
    l4.append(l1[i])
    l4.append(l2[i])
    l4.append(l3[i])

print(l1)
print(l2)
print(l3)
print(l4)