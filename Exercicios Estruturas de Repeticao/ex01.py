nota = float(input("Digite uma nota de 0 a 10: "))

while (nota < 0 or nota > 10):
    print("Nota inválida, por favor digite um valor de 0 a 10")
    nota = float(input("Digite uma nota de 0 a 10: "))

if (nota >= 0 or nota <= 10 ):
    print(f"A nota é {nota: .2f}")   