'''
Crie um programa que leia uma quantidade de números reais informada pelo usuário earmazene-os em uma lista valores.
Em seguida, crie uma lista stats vazia
● adicione na lista stats o menor valor da lista
● adicione na lista stats o maior valor da lista
● adicione na lista stats a soma dos elementos da lista
imprima o conteúdo na lista stats no seguinte padrão:
“menor valor: ____
maior valor: ___
Soma dos valores: ___”
'''

valores = []
stats = []

for i in range(10):
    num = float(input('Informe um número: '))
    valores.append(num)

stats.append(min(valores))
stats.append(max(valores))

print(f'''
Menor Valor: {min(valores)}
Maior Valor: {max(valores)}
Soma dos valores: {sum(stats)}
''')