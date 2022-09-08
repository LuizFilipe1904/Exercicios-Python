a = 80000
b = 200000
ano = 0

while (a < b):
    ano += 1
    a = a + (a * 0.03)
    a = int(a)
    b = b + (b * 0.015)
    b = int(b)
    #print(f'Após {ano} anos o país A ultrapassou o país B em número de habitantes.')
    #print(f'População de A: {a}')
    #print(f'População de B: {b}')

print(f'Após {ano} anos o país A ultrapassou o país B em número de habitantes.')
print(f'População de A: {a}')
print(f'População de B: {b}')
