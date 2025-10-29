import os
import time
import json

RELATORIO_JSON = "relatorio.json"

def salvar_relatorio_json(relatorio):
    with open(RELATORIO_JSON, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, ensure_ascii=False, indent=4)
        
def carregar_relatorio_json():
    if not os.path.exists(RELATORIO_JSON):
        return {}

    if os.path.getsize(RELATORIO_JSON) == 0:
        return {}

    with open(RELATORIO_JSON, "r", encoding="utf-8") as f:
        relatorio = json.load(f)

    return relatorio