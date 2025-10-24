import os
import time
import json
from utils import Utils

class Produtos:
    def __init__(self, nome, quantidade, preco, codigo):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.codigo = codigo

    def __str__(self):
        return f"Nome: {self.nome}\nCategoria: {self.categoria}\nQuantidade: {self.quantidade}\nPreco: {self.preco}\nCodigo: {self.codigo}"
    

class Limpeza(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, categoria="Limpeza"):
        super().__init__(nome, quantidade, preco, codigo)
        self.categoria = categoria

class Alimentos_frescos(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, categoria="Alimentos_frescos"):
        super().__init__(nome, quantidade, preco, codigo)
        self.categoria = categoria

class higiene_pessoal(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, categoria="Higiene_pessoal"):
        super().__init__(nome, quantidade, preco, codigo)
        self.categoria = categoria

class Carnes(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, categoria="Carnes",tipo_corte=None):
        super().__init__(nome, quantidade, preco, codigo)
        self.categoria = categoria
        self.tipo_corte = tipo_corte

class Bebidas(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, categoria="Bebidas"):
        super().__init__(nome, quantidade, preco, codigo)
        self.categoria = categoria

def inserir_produto():
    Utils.limpar_tela()
    print("=== Inserir Produto ===")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    codigo = input("Digite o código do produto: ")
    print("Selecione a categoria do produto:")
    categorias = ["Limpeza", "Alimentos_frescos", "Higiene_pessoal", "Carnes", "Bebidas"]
    for i in range(len(categorias)):
        print(f"{i+1} - {categorias[i]}")
    escolha = int(input("Digite o número da categoria: "))
    
    if escolha == 1:
        produto = Limpeza(nome, quantidade, preco, codigo)
    elif escolha == 2:
        produto = Alimentos_frescos(nome, quantidade, preco, codigo)
    elif escolha == 3:
        produto = higiene_pessoal(nome, quantidade, preco, codigo)
    elif escolha == 4:
        tipo_corte = input("Digite o tipo de corte da carne: ")
        produto = Carnes(nome, quantidade, preco, codigo, tipo_corte=tipo_corte)
    elif escolha == 5:
        produto = Bebidas(nome, quantidade, preco, codigo)
    else:
        print("Categoria inválida!")
        return None

    print("Produto inserido com sucesso!")
    time.sleep(2)
    return produto