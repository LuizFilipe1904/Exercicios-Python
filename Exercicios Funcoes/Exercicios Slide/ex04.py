'''
Escreva uma função que receba uma lista e retorne uma lista de listas com a lista original, 
a lista invertida e a lista ordenada
'''


def lista(vetor):
    ord = sorted(vetor)
    inv = sorted(vetor, reverse=True)
    todas = [[vetor], [inv], [ord]]
    print(todas)
    #return todas


numeros = []
while True:
    numeros.append(int(input("Digite um número: ")))
    resp = input('Deseja continuar? (S)Sim / (N)Não: ')
    resp = resp.upper()
    if resp == 'N':
        break

listas = lista(numeros)