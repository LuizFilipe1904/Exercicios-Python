usuario = input("Digite um nome de usuário: ")
senha = input("Digite a senha: ")

while (usuario == senha):
    print("Usuário e senha são iguais, eles devem ser diferentes. Tente novamente:")
    usuario = input("Digite um nome de usuário: ")
    senha = input("Digite a senha: ")

if (usuario != senha):
    print("Tudo certo com seus dados!")
