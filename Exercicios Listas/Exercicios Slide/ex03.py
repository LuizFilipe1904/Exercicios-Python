'''
Faça um programa que leia palavras e crie uma lista de strings e
depois adicione em uma lista “filtro” vazia somente as strings que se iniciem por uma letra escolhida pelo usuário.
'''

palavras = []
filtro = []

for i in range(5):
    print(f'Palavra {i + 1}:')
    palavra = input('Digite uma palavra: ')
    palavras.append(palavra)

letra = input('Informe a letra que deseja filtrar: ')