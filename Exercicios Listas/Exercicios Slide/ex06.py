'''
Escreva um programa que crie uma lista com todos a sequência de Fibonacci até o termo que seu usuário desejar.
'''

n = int(input('Informe até qual número deseja gerar a sequência de Fibonacci: '))
seq = []
ult = 1
pen = 1

if n == 1 or n == 2:
    print('1')
else:
    for i in range(2, n):
        termo = ult + pen
        pen = ult
        ult = termo
        i += 1
        seq.append(termo)

print(termo)