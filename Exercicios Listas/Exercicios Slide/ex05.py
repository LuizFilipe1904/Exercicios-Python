'''
Escreva um programa que receba uma lista de naipes e uma lista de valores e
gere a partir da combinação das duas listas uma listas de cartas. 
Use o baralho tradicional para gerar. ex: valor: 'A', nipe: 'copas', itemCarta: 'A de copas'
'''

import itertools
from itertools import permutations

naipes = ['Copas', 'Espadas', 'Ouro', 'Paus']
valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
cartas = []

permut = itertools.permutations(valores, len(naipes)) #Fez as permutas dos valores

for comb in permut: #Para cada permuta em permut faça:
    zipped = zip(comb, naipes) #Zipou todas as permutas com os naipes
    cartas.append(list(zipped)) #Adicionou as permutas zipadas com os naipes na lista cartas

print(cartas)