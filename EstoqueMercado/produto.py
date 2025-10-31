import os
import time
import json
from utils import Utils
from relatorio import carregar_relatorio_json, salvar_relatorio_json


ARQUIVO_JSON = "produtos.json"

class Produtos:
    def __init__(self, nome, quantidade, preco, codigo,data_de_fabricacao,data_de_validade):        
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.codigo = codigo
        self.data_de_fabricacao = data_de_fabricacao
        self.data_de_validade = data_de_validade

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"Nome: {self.nome}\nCategoria: {self.categoria}\nQuantidade: {self.quantidade}\nPreço: {self.preco}\nCódigo: {self.codigo} \nData de Fabricação: {self.data_de_fabricacao}\nData de Validade: {self.data_de_validade}"


class Limpeza(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, data_de_fabricacao, data_de_validade, categoria="Limpeza"):
        super().__init__(nome, quantidade, preco, codigo, data_de_fabricacao, data_de_validade)
        self.categoria = categoria


class Alimentos(Produtos):
    def __init__(self, nome, quantidade, preco, codigo,data_de_fabricacao, data_de_validade, categoria="Alimentos"):
        super().__init__(nome, quantidade, preco, codigo,data_de_fabricacao, data_de_validade)
        self.categoria = categoria


class higiene_pessoal(Produtos):
    def __init__(self, nome, quantidade, preco, codigo,data_de_fabricacao, data_de_validade,categoria="Higiene_pessoal"):
        super().__init__(nome, quantidade, preco, codigo,data_de_fabricacao, data_de_validade)
        self.categoria = categoria


class Carnes(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, data_de_fabricacao, data_de_validade, categoria="Carnes"):
        super().__init__(nome, quantidade, preco, codigo,data_de_fabricacao, data_de_validade)
        self.categoria = categoria

class Bebidas(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, data_de_fabricacao, data_de_validade,categoria="Bebidas"):
        super().__init__(nome, quantidade, preco, codigo,data_de_fabricacao, data_de_validade)
        self.categoria = categoria

class Objetos(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, data_de_fabricacao, data_de_validade, categoria="Objetos"):
        super().__init__(nome, quantidade, preco, codigo,data_de_fabricacao, data_de_validade)
        self.categoria = categoria

class Frutas(Produtos):
    def __init__(self, nome, quantidade, preco, codigo, data_de_fabricacao, data_de_validade, categoria="Frutas"):
        super().__init__(nome, quantidade, preco, codigo,data_de_fabricacao, data_de_validade)
        self.categoria = categoria