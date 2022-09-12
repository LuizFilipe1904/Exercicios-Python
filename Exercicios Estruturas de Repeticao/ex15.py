'''
A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n-ésimo termo.
'''

n = int(input("Informe qual número da sequência deseja saber: "))
primeiro = 1
segundo = 1

while (n <= 0):
    print('Por favor, digite um número positivo ou maior que zero.')
    n = int(input("Informe qual número da sequência deseja saber: "))

if (n == 1 or n == 2):
    print('1')
else:
    for i in range(2, n):
        termo = primeiro + segundo
        segundo = primeiro
        primeiro = termo
    print(termo)
