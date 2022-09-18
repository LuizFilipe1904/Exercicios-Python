'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

num = int(input("Digite um número inteiro: "))
divs = 0

for i in range (2, num):
    if num % i == 0:
        divs +=1

if divs == 0:
    print("O número digitado é primo!")
else:
    print("O número digitado não é primo!")
  
    