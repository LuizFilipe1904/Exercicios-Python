letra = input('Digite uma letra: ')
letra = letra.lower()

vogal = "aeiou"
consoante = 'qwrtyplkjhgfdsazxcvbnm'

if(letra in vogal):
    print(f'Sua letra é uma vogal, a letra digitada foi {letra}')

elif(letra in consoante):
    print(f'Sua letra é uma consoante, a letra digitada foi {letra}')

else:
    print('Você não digitou uma letra!')

