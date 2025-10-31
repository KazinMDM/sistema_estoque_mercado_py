import time
import json
import os
from utils import Utils
from inserir import cadastrar_produto, carregar_produtos_json
from dados import remover_produto, autenticar_usuario
from relatorio import menu_relatorio
from atualizacoes import atualizar_produto
from visualizar import visualizar_estoque
from cadastro import Cadastro

usuario_logado = None

def menu_inicial():
    global usuario_logado
    opc=["Cadastrar funcionário", "Login na conta", "Sair"]
    for i in range(len(opc)):
        print(f"{i+1} - {opc[i]}")
    resp = int(input("Digite a opção desejada: "))
    if resp == 1:
        Cadastro.cadastro()
    elif resp == 2:
        nome = input("Digite seu nome de usuário: ").strip().capitalize()
        senha = input("Digite sua senha: ").strip()
        usuario_logado = autenticar_usuario(nome, senha)
        if usuario_logado:
            print(f"Login bem-sucedido! Bem-vindo, {usuario_logado['nome']}!")
            cargo = usuario_logado.get("cargo")
            if cargo == "Gerente":
                menu_gerente()
            elif cargo == "Caixa":
                print("Acesso restrito para Caixa. Função em desenvolvimento.")



def menu_gerente():
    lista_produtos = carregar_produtos_json()    
    print(f"Olá Gerente, seja bem vindo ao Sistema de Estoque de Mercado!")
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

def menu_caixa():
    lista_produtos = carregar_produtos_json()    
    print("Olá, seja bem vindo ao Sistema de Estoque de Mercado!")
    while True:
        opcoes = ["Inserir produtos", "Remover produtos",  "Visulizar Estoque", "Sair"]
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
            visualizar_estoque(lista_produtos)

if __name__ == '__main__':
    menu_inicial()
    