'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
'''

base = int(input("Digite o número base: "))
exp = int(input("Digirte o expoente: "))
pot = 1

for i in range(exp):
    pot *= base

print(f"O resultado foi de {pot}")
