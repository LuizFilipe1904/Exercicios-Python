'''
Crie uma lista palavras com dez palavras e em seguida.
a. crie uma nova lista ord com o conteúdo de palavras em ordem alfabética
b. crie uma lista inv com o conteúdo de ord em ordem inversa.
c. imprima palavras, ord e inv
'''
palavras = ['uva', 'maçã', 'pera', 'manga', 'goiaba', 'mamão', 'melancia', 'morango', 'abacate', 'pinha']
ord = sorted(palavras)
inv = sorted(palavras, reverse = True)

print(f'''
Palavras: {palavras}\n
Em ordem alfabética: {ord}\n
Invertida: {inv}
''')