'''
Escreva uma função que receba um número e imprima sua tabuada
'''

def tabuada(num):
    print(f'tabuada do {num}:')
    for i in range(11):
        res = num * i
        print(f'{i} x {num} = {res}')

n = int(input('Informe o número que deseja calcular a tabuada: '))
tab = tabuada(n)