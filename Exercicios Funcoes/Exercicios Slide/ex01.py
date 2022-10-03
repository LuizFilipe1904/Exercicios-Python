'''
Uma função média que retorne a média dos elementos de uma lista
'''


def media(vet):
    soma = 0
    for i in range(len(vet)):
        soma += vet[i]
    media = soma / len(vet)
    return [soma, media]


lst = []
while True:
    lst.append(int(input('Digite um número: ')))
    resp = input('Deseja continuar? (S)sim / (N)não: ')
    resp = resp.upper()
    if resp == 'N':
        break

sm = media(lst)
print(f'A soma dos valores é {sm[0]} e a média é {sm[1]}.')