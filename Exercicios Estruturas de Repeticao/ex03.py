nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
sal = float(input("Digite seu salário: "))
sexo = input('''Digite seu sexo: 
f - feminino
m - masculino
Opção: ''')
sexo = sexo.lower()
ec = input('''Informe seu estado civil: 
s - solteiro(a)
c - casado(a)
v - viuvo(a)
d - divorciado(a)
Opção: ''')
ec = ec.lower()

while (len(nome) <= 3):
    print("O nome deve conter mais de três letras. Tente novamente.")
    nome = input("Digite seu nome: ")

while (idade < 0 or idade > 150):
    print("Idade inválida, digite uma idade entre 0 e 150.")
    idade = int(input("Digite sua idade: "))

while (sal < 0):
    print('Salário inválido, tente novamente.')
    sal = float(input("Digite seu salário: "))

while (sexo != "f" and sexo != "m"):
    print("Sexo inválido. Tente novamente.")
    sexo = input('''Digite seu sexo: 
    f - feminino
    m - masculino
    Opção: ''')

while (ec != 'c' and ec != 's' and ec != 'v' and ec != 'd'):
    print("Estado civíl inválido, tente novamente.")
    ec = input('''Informe seu estado civil: 
    s - solteiro(a)
    c - casado(a)
    v - viuvo(a)
    d - divorciado(a)
    Opção: ''')
