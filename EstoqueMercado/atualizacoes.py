import time
from utils import Utils
from inserirRemoverProdutos import salvar_produtos_json

def atualizar_produto(lista_produtos):
    Utils.limpar_tela()
    print("=== Atualizar Produto ===")
    codigo = input("Digite o código do produto que deseja atualizar: ")

    produto_encontrado = None
    for produto in lista_produtos:
        if produto.codigo == codigo:
            produto_encontrado = produto
            break

    if not produto_encontrado:
        print("Produto não encontrado!")
        time.sleep(2)
        return lista_produtos

    Utils.limpar_tela()
    print(f"Nome do produto: {produto_encontrado.nome}")
    print(f"Categoria: {produto_encontrado.categoria}")
    print(f"Preço atual: R${produto_encontrado.preco}")
    print(f"Quantidade atual: {produto_encontrado.quantidade}")
    print("----------------------------------")

    print("O que você deseja atualizar?")
    print("1 - Nome")
    print("2 - Preço")
    print("3 - Quantidade")
    print("0 - Cancelar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        antigo_nome = produto_encontrado.nome
        novo_nome = input("Digite o novo nome: ").strip()
        produto_encontrado.nome = novo_nome
        print(f"\nNome atualizado com sucesso!")
        print(f"Antes: {antigo_nome}")
        print(f"Depois: {produto_encontrado.nome}")

    elif opcao == 2:
        antigo_preco = produto_encontrado.preco
        novo_preco = float(input("Digite o novo preço: "))
        produto_encontrado.preco = novo_preco
        print(f"\nPreço atualizado com sucesso!")
        print(f"Antes: R${antigo_preco}")
        print(f"Depois: R${produto_encontrado.preco}")

    elif opcao == 3:
        antiga_qtd = produto_encontrado.quantidade
        nova_quantidade = int(input("Digite a nova quantidade: "))
        produto_encontrado.quantidade = nova_quantidade
        print(f"\nQuantidade atualizada com sucesso!")
        print(f"Antes: {antiga_qtd}")
        print(f"Depois: {produto_encontrado.quantidade}")

    elif opcao == 0:
        print("Atualização cancelada.")
        time.sleep(2)
        return lista_produtos
    else:
        print("Opção inválida!")
        time.sleep(2)
        return lista_produtos

    salvar_produtos_json(lista_produtos)

    print("\nAlterações salvas com sucesso!")
    print("----------------------------------")
    print(f"Produto atualizado:\n"
          f"Nome: {produto_encontrado.nome}\n"
          f"Categoria: {produto_encontrado.categoria}\n"
          f"Preço: R${produto_encontrado.preco}\n"
          f"Quantidade: {produto_encontrado.quantidade}")
    
    time.sleep(3)
    return produto
    