numeros = []
soma = 0

for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)
    soma += numero

media = soma / 5
print(f'A soma é de {soma} e a média é {media}')

    