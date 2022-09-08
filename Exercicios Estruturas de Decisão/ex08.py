preco1 = float(input('Informe o preço do primeiro produto: '))
preco2 = float(input('Informe o preço do segundo produto: '))
preco3 = float(input('Informe o preço do terceiro produto: '))

if (preco1 < preco2 and preco1 < preco3):
    print('O produto 1 é mais barato!')

elif (preco2 < preco1 and preco2 < preco3):
    print('O produto 2 é mais barato!')

elif (preco3 < preco1 and preco3 < preco2):
    print('O produto 3 é mais barato!')

elif (preco1 == preco2 and preco2 < preco3):
    print('Os produtos 1 e 2 são mais baratos!')

elif (preco1 == preco3 and preco3 < preco2):
    print('Os produtos 1 e 3 são mais baratos!')

elif (preco2 == preco3 and preco3 < preco1):
    print('Os produtos 2 e 3 são mais baratos!')

else:
    print('Todos os preços são iguais!')
