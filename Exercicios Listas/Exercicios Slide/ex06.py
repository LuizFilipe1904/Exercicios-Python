'''
Escreva um programa que crie uma lista com todos a sequência de Fibonacci até o termo que seu usuário desejar.
'''

n = int(input('Quantos números deseja mostrar: '))
t1 = 1
t2 = 1
seq = [1, 1]

for cont in range(2, n):
    t3 = t1 + t2
    t2 = t1
    t1 = t3
    seq.append(t3)
print(seq)
