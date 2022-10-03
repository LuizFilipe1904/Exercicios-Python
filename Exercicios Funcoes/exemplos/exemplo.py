def SomaeMedia(vet):
    '''
    Função que soma e calcula a media de valores de uma lista
    '''
    soma = 0
    for i in range(len(vet)):
        soma += vet[i]
    media = soma / len(vet)
    return [soma, media]


lst = []
while True:
    lst.append(int(input('Digite um valor: ')))
    resp = input('Deseja continuar? (S)sim / (N)não')
    resp = resp.upper()
    if resp == 'N':
        break

sm = SomaeMedia(lst)
print(f'O conjunto de dados possui soma {sm[0]} e média {sm[1]}')
help(SomaeMedia)
