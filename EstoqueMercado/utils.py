import os
import time
import json

ARQUIVO_JSON = "produtos.json"

class Utils:
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # def salvar_produtos_json(lista_produtos):
    #     with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
    #         json.dump([p.to_dict() for p in lista_produtos], f, ensure_ascii=False, indent=4)

    # def carregar_produtos_json():
    #     if not os.path.exists(ARQUIVO_JSON):
    #         return []
    #     if os.path.getsize(ARQUIVO_JSON) == 0:
    #         return []
    #     with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
    #         dados = json.load(f)
    #     lista_produtos = []
    #     for item in dados:
    #         categoria = item.get("categoria")
    #         if categoria == "Limpeza":
    #             produto = Limpeza(**item)
    #         elif categoria == "Alimentos_frescos":
    #             produto = Alimentos_frescos(**item)
    #         elif categoria == "Higiene_pessoal":
    #             produto = higiene_pessoal(**item)
    #         elif categoria == "Carnes":
    #             produto = Carnes(**item)
    #         elif categoria == "Bebidas":
    #             produto = Bebidas(**item)
    #         elif categoria == 'Objetos':
    #             produto = Objetos(**item)
    #         else:
    #             produto = Produtos(**item)
    #         lista_produtos.append(produto)

    #     return lista_produtos