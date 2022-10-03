'''
Uma função ehPrimo que leia um inteiro positivo e retorne um valor lógico True se o número for primo ou False, caso contrário.
'''


def ehPrimo(num):
    mult = 0
    for i in range(2, num):
        if num % i == 0:
            mult += 1
        if mult == 0:
            return True
        else:
            return False


n = int(input('Informe o número que deseja saber se é primo: '))
primo = ehPrimo(n)
print(f'{primo}')
