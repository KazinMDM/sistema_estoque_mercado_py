import time
import json
import os
from relatorio import salvar_relatorio_json
from utils import Utils
from dados import salvar_produtos_json
from produto import Produtos, Limpeza, Alimentos, higiene_pessoal, Carnes, Bebidas, Objetos, Frutas

def remover_produto(lista_produtos):
    Utils.limpar_tela()
    print("=== Remover Produto ===")
    codigo = input("Digite o código do produto que deseja remover: ")

    produto_encontrado = None
    for produto in lista_produtos:
        if produto.codigo == codigo:
            produto_encontrado = produto
            break

    if not produto_encontrado:
        print("Produto não encontrado!")
        time.sleep(2)
        return lista_produtos

    print("\nProduto encontrado:")
    print(f"Nome: {produto_encontrado.nome}")
    print(f"Código: {produto_encontrado.codigo}")
    print(f"Categoria: {produto_encontrado.categoria}")
    print("-----------------------------")

    confirmar = input("Deseja realmente remover este produto? (S/N): ").strip().lower()
    confirmacao = ["s", "sim", "ss"]
    if confirmar in confirmacao:
        lista_produtos.remove(produto_encontrado)
        salvar_produtos_json(lista_produtos)
        salvar_relatorio_json({"acao": "remover_produto", "produto": produto.to_dict(), "Data": time.strftime("%Y-%m-%d | %H:%M:%S")})
        print("Produto removido com sucesso!")
    else:
        print("Remoção cancelada.")
    
    time.sleep(2)
    if deseja_voltar := input("\nDeseja voltar ao menu principal? (S/N): ").strip().upper() == 'S':
        Utils.limpar_tela()
        return lista_produtos
    else:
        Utils.limpar_tela()
        print("Saindo do sistema...")
        exit()

