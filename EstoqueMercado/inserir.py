import os
import time
import json
from utils import Utils
from dados import salvar_produtos_json, carregar_produtos_json
from relatorio import salvar_relatorio_json
from relatorio import carregar_relatorio_json, salvar_relatorio_json
from produto import Produtos, Limpeza, Alimentos, higiene_pessoal, Carnes, Bebidas, Objetos, Frutas


def cadastrar_produto(lista_produtos):
    Utils.limpar_tela()
    print("=== Inserir Produto ===")
    nome = input("Digite o nome do produto: ").lower().capitalize()
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    codigo = input("Digite o código do produto: \n [quantidade de caracteres: 5] \n--> ")
    data_de_fabricacao = input("Digite a data de fabricação do produto (DD/MM/AAAA): ")
    data_de_validade = input("Digite a data de validade do produto (DD/MM/AAAA): ")
    while len(codigo) != 5:
        print("Código inválido! \nO código deve ter exatamente 5 caracteres.")
        codigo = input("Digite o código do produto: \n [quantidade de caracteres: 5] \n--> ")
    print("Selecione a categoria do produto:")
    categorias = ["Limpeza", "Alimentos", "Higiene_pessoal", "Carnes", "Bebidas", "Objetos","Frutas"]
    for i in range(len(categorias)):
        print(f"{i+1} - {categorias[i]}")
    escolha = int(input("Digite o número da categoria: "))
    
    if escolha == 1:
        Utils.limpar_tela()
        produto = Limpeza(nome, quantidade, preco, codigo, data_de_fabricacao, data_de_validade, categoria="Limpeza")
    elif escolha == 2:
        Utils.limpar_tela()
        produto = Alimentos(nome, quantidade, preco, codigo, data_de_fabricacao, data_de_validade, categoria="Alimentos")
    elif escolha == 3:
        Utils.limpar_tela()
        produto = higiene_pessoal(nome, quantidade, preco, codigo, data_de_fabricacao, data_de_validade,categoria="Higiene_pessoal")
    elif escolha == 4:
        Utils.limpar_tela()
        produto = Carnes(nome, quantidade, preco, codigo,data_de_fabricacao ,data_de_validade, categoria="Carnes")
    elif escolha == 5:
        Utils.limpar_tela()
        produto = Bebidas(nome, quantidade, preco, codigo,data_de_fabricacao ,data_de_validade, categoria="Bebidas")
    elif escolha == 6:
        Utils.limpar_tela()
        produto = Objetos(nome, quantidade, preco, codigo,data_de_fabricacao ,data_de_validade, categoria="Objetos")
    elif escolha == 7:
        Utils.limpar_tela()
        produto = Frutas(nome, quantidade, preco, codigo,data_de_fabricacao ,data_de_validade, categoria="Frutas")
    else:
        print("Categoria inválida!")
        return lista_produtos
    
    lista_produtos.append(produto)
    salvar_produtos_json(lista_produtos)
    salvar_relatorio_json({"acao": "inserir_produto", "produto": produto.to_dict(), "Data": time.strftime("%Y-%m-%d | %H:%M:%S")})

    print("Produto inserido com sucesso!")

    time.sleep(2)
    if deseja_voltar := input("\nDeseja voltar ao menu principal? (S/N): ").strip().upper() == 'S':
        Utils.limpar_tela()
        return lista_produtos
    else:
        Utils.limpar_tela()
        print("Saindo do sistema...")
        exit()