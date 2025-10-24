import os
import time
import json

class Utils:
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

    def carregar_dados(caminho_arquivo):
        if not os.path.exists(caminho_arquivo):
            return {}
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        return dados
    
    def salvar_dados(caminho_arquivo, dados):
        with open(caminho_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
        