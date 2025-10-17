def menu_principal():
    opcoes = ["Gerenciar Estoque", "Visulizar Estoque", "Sair"]
    print("Olá, seja bem vindo ao Sistema de Estoque de Mercado!")
    for i in range(len(opcoes)):
        if opcoes[i] == "Sair":
            print(f"0 - {opcoes[i]}")
        else:
            print(f"{i+1} - {opcoes[i]}")

if __name__ == '__main__':
    menu_principal() 