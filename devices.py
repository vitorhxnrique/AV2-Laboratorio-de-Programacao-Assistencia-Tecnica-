aparelhos = []
def cadastrar_aparelhos():
    print("\n--- Cadastro de Aparelho ---")
    nome = input("Digite o nome do aparelho: ")
    aparelhos.append({"nome": nome})
    print(f"Aparelho '{nome}' cadastrado com sucesso!")

def editar_aparelhos():
    print("\n--- Edição de Aparelhos ---")
    exibir_aparelhos()
    nome = input("Digite o nome do Aparelho que deseja editar: ")
    for p in aparelhos:
        if p["nome"] == nome:
            novo_nome = input(f"Digite o novo nome para '{nome}' (ou aperte Enter para manter): ")
            if novo_nome:
                p["nome"] = novo_nome
            print(f"Aparelho '{nome}' atualizado com sucesso!")
            return
    print("Aparelho não encontrado.")

def exibir_aparelhos():
    print("\n--- Lista de Aparelhos ---")
    if not aparelhos:
        print("Nenhum Aparelho cadastrado.")
    else:
        for i, p in enumerate(aparelhos, 1):
            print(f"{i}. nome: {p['nome']}")

def excluir_aparelhos():
    print("\n--- Exclusão de Aparelhos ---")
    exibir_aparelhos()
    nome = input("Digite o nome do aparelho que deseja excluir: ")
    for p in aparelhos:
        if p["nome"] == nome:
            aparelhos.remove(p)
            print(f"Aparelho '{nome}' excluído com sucesso!")
            return
    print("Aparelho não encontrado.")

