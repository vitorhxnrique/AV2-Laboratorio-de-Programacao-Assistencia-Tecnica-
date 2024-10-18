from devices import cadastrar_aparelhos, editar_aparelhos, exibir_aparelhos, excluir_aparelhos
from menu import menu_principal

def cadastrar_usuario():    
    print("Bem vindo ao sistema de produtos, cadastre seu usuario")
    usuario = input("Digite o nome de usuario que deseja: ")
    senha = input("Digite a senha desejada: ")

    dicionario[usuario] = senha

def login():
    global logon
    TentativaUsuario = input("Digite o seu user correto: ")
    TentativaSenha = input("Digite a senha correta: ")
    
    if TentativaUsuario in  dicionario and dicionario[TentativaUsuario] == TentativaSenha:
        print(f"bem vindo, {TentativaUsuario}")
        logon += 1
    else:
        print("user ou senha invalidos")

dicionario = {}
aparelhos = []
logon = 0 





print("\n---Bem vindo ao Sistema!---")
print("1. Cadastro")
print("2. Login")
choice = None
while type (choice) is not int or choice <= 0 or choice > 2:
    try:
        choice = int(input("Escolha sua opção: "))
    except: 
        print("Escolha 1 ou 2")        
while True:
    if choice == 1:
        cadastrar_usuario()
        login()
    elif choice == 2:
        login()

    break
if logon == 1:
    menu_principal()


