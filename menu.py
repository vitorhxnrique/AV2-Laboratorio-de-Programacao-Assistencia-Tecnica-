from devices import cadastrar_aparelhos, editar_aparelhos, exibir_aparelhos, excluir_aparelhos
def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastrar Aparelho")
        print("2. Editar Aparelho")
        print("3. Exibir Aparelho")
        print("4. Excluir Aparelho")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aparelhos()
        elif opcao == "2":
            editar_aparelhos()
        elif opcao == "3":
            exibir_aparelhos()
        elif opcao == "4":
            excluir_aparelhos()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
