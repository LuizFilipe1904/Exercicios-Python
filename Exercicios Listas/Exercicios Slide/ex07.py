'''
Crie um programa que:
Crie três listas:
a.par com os números pares de 10 a 200
b.impar com os números ímpares de 10 a 200
c.num que seja união concatenada e ordenada das listas par e impar
'''

numeros = list(range(10, 201))
pares = []
impares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

num = pares + impares
num.sort()

print(f'''
Pares: {pares}\n
Impares: {impares}\n
Todos os números: {num}

''')
