ano = 0
a = int(input("Digite a população do país A: "))
b = int(input("Digite a população do país B: "))
tax_a = float(input('Informe a taxa de crescimento do país A: '))
tax_b = float(input('Informe a taxa de crescimento do país B: '))

while (a < b):
    ano += 1
    a = a + (a * tax_a)
    b = b + (b * tax_b)
    
print(f'Após {ano} anos o país A ultrapassou o país B em número de habitantes.')
print(f'População de A: {a}')
print(f'População de B: {b}')
