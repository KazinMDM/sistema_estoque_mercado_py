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
    
class Limpeza: