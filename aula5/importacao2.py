from funcoes import login

while True:
    usuario = input('Digite o nome do usuario: ')
    senha = input("Digite a senha do usuario: ")

    if login(usuario,senha):
        print("logado com sucesso")
        break
    else:
        print('Tente Novamente')