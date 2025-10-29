import time
import json
import os
from utils import Utils
from inserirRemoverProdutos import (
    cadastrar_produto,
    remover_produto,
    carregar_produtos_json
)
from atualizacoes import atualizar_produto
from visualizar import visualizar_estoque
from relatorio import menu_relatorio




def menu_principal():
    lista_produtos = carregar_produtos_json()    
    print("Olá, seja bem vindo ao Sistema de Estoque de Mercado!")
    while True:
        opcoes = ["Inserir produtos", "Remover produtos", "Atualizar informações do produtos", "Visulizar Estoque", "Relatório de estoque", "Sair"]
        time.sleep(1)
        print("O que você deseja fazer?")
        time.sleep(1)
        for i in range(len(opcoes)):
            if opcoes[i] == "Sair":
                print(f"0 - {opcoes[i]}")
                time.sleep(1.5)
            else:
                print(f"{i+1} - {opcoes[i]}")
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
        elif resp == 5:
            menu_relatorio()

if __name__ == '__main__':
    menu_principal() 