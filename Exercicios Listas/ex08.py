'''
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
'''

idades = []
alturas = []

for i in range(5):
    print(f'Pessoa {i + 1}')
    idade = int(input('Informe sua idade: '))
    alt = float(input('Informe sua altura: '))

    while idade < 0:
        idade = int(input('Idade inválida, tente novamente: '))
    while alt < 0:
        alt = float(input('Altura inválida, tente novamente: '))

    idades.append(idade)
    alturas.append(alt)

idades.reverse()
alturas.reverse()

print(f'Idades: {idades: .2f}')
print(f'Alturas: {alturas: .2f}')
