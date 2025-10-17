def menu_principal():
    opcoes = ["Inserir produtos", "Remover produtos", "Atualizar informações do produtos", "Visulizar Estoque", "Buscar produto", "Sair"]
    print("Olá, seja bem vindo ao Sistema de Estoque de Mercado!")
    for i in range(len(opcoes)):
        if opcoes[i] == "Sair":
            print(f"0 - {opcoes[i]}")
        else:
            print(f"{i+1} - {opcoes[i]}")
    resp = int(input("Digite a opção desejada: "))
    return resp

if __name__ == '__main__':
    menu_principal() 