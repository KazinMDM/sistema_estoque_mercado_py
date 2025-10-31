import time
import json
import os
from utils import Utils
from relatorio import salvar_relatorio_json
from produto import Produtos, Limpeza, Alimentos, higiene_pessoal, Carnes, Bebidas, Objetos, Frutas

ARQUIVO_JSON = "produtos.json"

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
        salvar_relatorio_json({"acao": "atualizar_nome_produto", "produto": produto_encontrado.to_dict(), "Data": time.strftime("%Y-%m-%d | %H:%M:%S")})

    elif opcao == 2:
        antigo_preco = produto_encontrado.preco
        novo_preco = float(input("Digite o novo preço: "))
        produto_encontrado.preco = novo_preco
        print(f"\nPreço atualizado com sucesso!")
        print(f"Antes: R${antigo_preco}")
        print(f"Depois: R${produto_encontrado.preco}")
        salvar_relatorio_json({"acao": "atualizar_preco_produto", "produto": produto_encontrado.to_dict(), "Data": time.strftime("%Y-%m-%d | %H:%M:%S")})

    elif opcao == 3:
        antiga_qtd = produto_encontrado.quantidade
        nova_quantidade = int(input("Digite a nova quantidade: "))
        produto_encontrado.quantidade = nova_quantidade
        print(f"\nQuantidade atualizada com sucesso!")
        print(f"Antes: {antiga_qtd}")
        print(f"Depois: {produto_encontrado.quantidade}")
        salvar_relatorio_json({"acao": "atualizar_quantidade_produto", "produto": produto_encontrado.to_dict(), "Data": time.strftime("%Y-%m-%d | %H:%M:%S")})

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
    print(
        f"Produto atualizado:\n"
        f"Nome: {produto_encontrado.nome}\n"
        f"Categoria: {produto_encontrado.categoria}\n"
        f"Preço: R${produto_encontrado.preco}\n"
        f"Quantidade: {produto_encontrado.quantidade}"
        )
    
    time.sleep(2)
    if deseja_voltar := input("\nDeseja voltar ao menu principal? (S/N): ").strip().upper() == 'S':
        Utils.limpar_tela()
        return lista_produtos
    else:
        Utils.limpar_tela()
        time.sleep(1)
        print("Saindo do sistema...")
        time.sleep(1)
        exit()


def salvar_produtos_json(lista_produtos):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in lista_produtos], f, ensure_ascii=False, indent=4)

def carregar_produtos_json():
    if not os.path.exists(ARQUIVO_JSON):
        return []

    if os.path.getsize(ARQUIVO_JSON) == 0:
        return []

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        dados = json.load(f)

    lista_produtos = []
    for item in dados:
        categoria = item.get("categoria")
        if categoria == "Limpeza":
            produto = Limpeza(**item)
        elif categoria == "Alimentos":
            produto = Alimentos(**item)
        elif categoria == "Higiene_pessoal":
            produto = higiene_pessoal(**item)
        elif categoria == "Carnes":
            produto = Carnes(**item)
        elif categoria == "Bebidas":
            produto = Bebidas(**item)
        elif categoria == 'Objetos':
            produto = Objetos(**item)
        elif categoria =='Frutas':
            produto = Frutas(**item)

        lista_produtos.append(produto)

    return lista_produtos