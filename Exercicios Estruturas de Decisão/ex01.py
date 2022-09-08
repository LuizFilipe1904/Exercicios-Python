l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceito lado: 5'))

if(l1 == l2 and l2 == l3):
    print('Seu triângulo é equilátero')

elif (l1 != l2 and l2 != l3 and l3 != l1):
    print('Seu triângulo é escaleno')

else:
    print('Seu triângulo é isóceles')