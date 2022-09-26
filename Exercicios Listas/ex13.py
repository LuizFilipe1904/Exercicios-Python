'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''

temps = []
meses = ['1 - Janeiro', '2 - Fevereiro', '3 - Março', '4 - Abril', '5 - Maio',
         '6 - Junho', '7 - Julho', '8 - Agosto', '9 - Setembro', '10 - Outubro', '11 - Novembro', '12 - Dezembro']
acima = {}

for i in range(len(meses)):
    print(f'Informe a temperatura do mês: {meses[i]}')
    temp = float(input('Informe a temperatura do mês: '))
    temps.append(temp)

soma = sum(temps)
media = soma / len(temps)

for i in range(len(meses)):
    if temp[i] > media:
        acima.update({meses[i] : temp[i]})

print(f'Média das temperaturas: {media}')
print(f'Meses com temperatura acima da média: {acima}')
