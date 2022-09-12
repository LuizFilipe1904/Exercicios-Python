'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
'''

usuario = input("Digite um nome de usuário: ")
senha = input("Digite a senha: ")

while (usuario == senha):
    print("Usuário e senha são iguais, eles devem ser diferentes. Tente novamente:")
    usuario = input("Digite um nome de usuário: ")
    senha = input("Digite a senha: ")

if (usuario != senha):
    print("Tudo certo com seus dados!")
