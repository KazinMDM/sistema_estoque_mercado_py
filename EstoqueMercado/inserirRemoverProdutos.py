import os
import time
import json

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
    def __init__(self, nome, quantidade, preco, codigo, categoria="Carnes"):
        super().__init__(nome, quantidade, preco, codigo)
        self.categoria = categoria

class Bebidas(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, categoria="Bebidas"):
        super().__init__(nome, quantidade, preco, codigo)
        self.categoria = categoria

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')