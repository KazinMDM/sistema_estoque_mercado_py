import json
import os
import time
from utils import Utils
from produto import Limpeza, Alimentos, higiene_pessoal, Carnes, Bebidas, Objetos, Frutas


ARQUIVO_JSON = "produtos.json"
__arquivo = "cadastro.json"

def salvar_produtos_json(lista_produtos):
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
        item.setdefault("data_de_fabricacao", "N/A")
        item.setdefault("data_de_validade", "N/A")
        if categoria == "Limpeza":
            produto = Limpeza(**item)
        elif categoria == "Alimentos":
            produto = Alimentos(**item)
        elif categoria == "Higiene_pessoal":
            produto = higiene_pessoal(**item)
        elif categoria == "Carnes":
            produto = Carnes(**item)
        elif categoria == "Bebidas":
            produto = Bebidas(**item)
        elif categoria == 'Objetos':
            produto = Objetos(**item)
        elif categoria =='Frutas':
            produto = Frutas(**item)

        lista_produtos.append(produto)

    return lista_produtos

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

    confirmar = input("Deseja realmente remover este produto? (S/N): ").strip().lower()
    confirmacao = ["s", "sim", "ss"]
    if confirmar in confirmacao:
        lista_produtos.remove(produto_encontrado)
        salvar_produtos_json(lista_produtos)
        print("Produto removido com sucesso!")
    else:
        print("Remoção cancelada.")
    
    time.sleep(2)
    if deseja_voltar := input("\nDeseja voltar ao menu principal? (S/N): ").strip().upper() == 'S':
        Utils.limpar_tela()
        return lista_produtos
    else:
        Utils.limpar_tela()
        print("Saindo do sistema...")
        exit()

def carregar_funcionario(cls):
    try:
        with open(cls.__arquivo, "r", encoding="utf-8") as arquivo:
            pessoas = json.load(arquivo)
            return pessoas
    except FileNotFoundError:
        return []

def salvar_funcionario(cls, funcionarios):
    with open(cls.__arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(funcionarios, arquivo, ensure_ascii=False, indent=4)
        arquivo.close()
    print("Pessoas salvas com sucesso!")

def autenticar_usuario(cls, nome, senha):
    funcionarios = cls.carregar_funcionario()
    for funcionario in funcionarios:
        if funcionario["nome"] == nome and funcionario["senha"] == senha:
            return True
    return False