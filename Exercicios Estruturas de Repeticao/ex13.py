base = int(input("Digite o número base: "))
exp = int(input("Digirte o expoente: "))
pot = 1

for i in range(exp):
    pot *= base

print(f"O resultado foi de {pot}")


