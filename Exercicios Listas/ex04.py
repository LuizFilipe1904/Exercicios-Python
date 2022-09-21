'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

consoante = []
vogal = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

for i in range(10):
    letra = input('Digite 10 caracteres: ')

    if letra not in vogal:
        consoante.append(letra)

print(f'Foram lidas {len(consoante)} consoantes.')
print(f'As consoantes lidas foram: {consoante}')