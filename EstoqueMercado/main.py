import time
import json
import os
from utils import Utils
from inserirRemoverProdutos import (
    inserir_produto,
    remover_produto,
    salvar_produtos_json,
    carregar_produtos_json
)

def menu_principal():
    lista_produtos = carregar_produtos_json()
    while True:
        opcoes = ["Inserir produtos", "Remover produtos", "Atualizar informações do produtos", "Visulizar Estoque", "Buscar produto", "Sair"]
        print("Olá, seja bem vindo ao Sistema de Estoque de Mercado!")
        for i in range(len(opcoes)):
            if opcoes[i] == "Sair":
                print(f"0 - {opcoes[i]}")
            else:
                print(f"{i+1} - {opcoes[i]}")
        resp = int(input("Digite a opção desejada: "))
        if resp == 0:
            print("Saindo do sistema...")
            break
        elif resp == 1:
            Utils.limpar_tela()
            produto = inserir_produto()
            if produto:
                lista_produtos.append(produto)
                salvar_produtos_json(lista_produtos)
          

if __name__ == '__main__':
    menu_principal() 