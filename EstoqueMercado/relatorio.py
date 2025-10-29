import os
import time
import json
from utils import Utils

RELATORIO_JSON = "relatorio.json"

def salvar_relatorio_json(novo_registro):
    relatorio_existente = []
    if os.path.exists(RELATORIO_JSON) and os.path.getsize(RELATORIO_JSON) > 0:
        with open(RELATORIO_JSON, "r", encoding="utf-8") as f:
            try:
                relatorio_existente = json.load(f)
                if not isinstance(relatorio_existente, list):
                    relatorio_existente = [relatorio_existente]
            except json.JSONDecodeError:
                relatorio_existente = []
    relatorio_existente.append(novo_registro)
    
    with open(RELATORIO_JSON, "w", encoding="utf-8") as f:
        json.dump(relatorio_existente, f, ensure_ascii=False, indent=4)


def carregar_relatorio_json():
    if not os.path.exists(RELATORIO_JSON):
        return {}

    if os.path.getsize(RELATORIO_JSON) == 0:
        return {}

    with open(RELATORIO_JSON, "r", encoding="utf-8") as f:
        relatorio = json.load(f)

    return relatorio

def limpar_relatorio_json():
    with open(RELATORIO_JSON, "w", encoding="utf-8") as f:
        f.write("")
    print("Relatório limpo com sucesso!")

def exibir_relatorio():
    relatorio = carregar_relatorio_json()
    if not relatorio:
        print("Nenhum relatório encontrado.")
        time.sleep(3)
        return

    print("========== Relatório de Estoque ==========")
    print(json.dumps(relatorio, indent=4, ensure_ascii=False))
    time.sleep(10)

def menu_relatorio():
    while True:
        print("=== Menu de Relatório ===")
        print("1 - Exibir relatório")
        print("2 - Limpar relatório")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_relatorio()
        elif opcao == "2":
            limpar_relatorio_json()
            time.sleep(2)
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")
            time.sleep(2)