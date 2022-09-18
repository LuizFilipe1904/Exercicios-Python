'''
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
'''

num = int(input("Digite um número inteiro: "))
divs = 0

for i in range (2, num):
    if num % i == 0:  # Verifica se o número digitado tem algum multiplo, além de 1 e ele próprio.
        print(f"Multiplo de {i}")
        divs +=1  

if divs == 0:  #Sem multiplos, portanto é primo.
    print("O número digitado é primo!")
else:
    print("O número digitado não é primo")