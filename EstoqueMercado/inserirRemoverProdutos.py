import os
import time
import json
from utils import Utils

ARQUIVO_JSON = "produtos.json"

def salvar_produtos_json(lista_produtos):
    """Salva a lista de produtos no arquivo JSON"""
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
        elif categoria == "Alimentos_frescos":
            produto = Alimentos_frescos(**item)
        elif categoria == "Higiene_pessoal":
            produto = higiene_pessoal(**item)
        elif categoria == "Carnes":
            produto = Carnes(**item)
        elif categoria == "Bebidas":
            produto = Bebidas(**item)
        elif categoria == 'Objetos':
            produto = Objetos(**item)
        else:
            produto = Produtos(**item)
        lista_produtos.append(produto)

    return lista_produtos

class Produtos:
    def __init__(self, nome, quantidade, preco, codigo):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.codigo = codigo

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"Nome: {self.nome}\nCategoria: {self.categoria}\nQuantidade: {self.quantidade}\nPreço: {self.preco}\nCódigo: {self.codigo}"


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
    def __init__(self, nome, quantidade, preco, codigo, categoria="Carnes", tipo_corte=None):
        super().__init__(nome, quantidade, preco, codigo)
        self.categoria = categoria
        self.tipo_corte = tipo_corte


class Bebidas(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, categoria="Bebidas"):
        super().__init__(nome, quantidade, preco, codigo)
        self.categoria = categoria


class Objetos(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, categoria="Objetos"):
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

    confirmar = input("Deseja realmente remover este produto? (S/N): ").strip().upper()
    if confirmar == "S":
        lista_produtos.remove(produto_encontrado)
        print("Produto removido com sucesso!")
    else:
        print("Remoção cancelada.")

    time.sleep(2)
    return lista_produtos
  
