import time
import json
import os
from utils import Utils
from inserirRemoverProdutos import (
    cadastrar_produto,
    remover_produto,
    salvar_produtos_json,
    carregar_produtos_json
)
from atualizacoes import atualizar_produto
from visualizar import visualizar_estoque




def menu_principal():
    lista_produtos = carregar_produtos_json()
    while True:
        opcoes = ["Inserir produtos", "Remover produtos", "Atualizar informações do produtos", "Visulizar Estoque", "Buscar produto", "Sair"]
        print("Olá, seja bem vindo ao Sistema de Estoque de Mercado!")
        time.sleep(1)
        print("O que você deseja fazer?")
        time.sleep(1)
        for i in range(len(opcoes)):
            if opcoes[i] == "Sair":
                print(f"0 - {opcoes[i]}")
                time.sleep(1.5)
            else:
                print(f"{i+1} - {opcoes[i]}")
                time.sleep(0.5)
        resp = int(input("Digite a opção desejada: "))
        if resp == 0:
            print("Saindo do sistema...")
            break
        elif resp == 1:
            lista_produtos = cadastrar_produto(lista_produtos) 
        elif resp == 2:
            lista_produtos = remover_produto(lista_produtos)
        elif resp == 3:
            lista_produtos = atualizar_produto(lista_produtos)
        elif resp == 4:
            visualizar_estoque(lista_produtos)

if __name__ == '__main__':
    menu_principal() 