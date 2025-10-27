import time
from utils import Utils

def visualizar_estoque(lista_produtos):
    Utils.limpar_tela()
    print("=== ESTOQUE ATUAL ===\n")

    if not lista_produtos:
        print("Nenhum produto cadastrado no sistema.")
        time.sleep(2)
        return lista_produtos

    for i, produto in enumerate(lista_produtos, 1):
        print(f"{i}. Nome: {produto.nome}")
        print(f"   Categoria: {produto.categoria}")
        print(f"   Quantidade: {produto.quantidade}")
        print(f"   Valor: R${produto.preco:.2f}")
        print(f"   Código: {produto.codigo}")
        print("-" * 40)

    print(f"\nTotal de produtos cadastrados: {len(lista_produtos)}")
    
    
    time.sleep(2)
    if deseja_voltar := input("\nDeseja voltar ao menu principal? (S/N): ").strip().upper() == 'S':
        Utils.limpar_tela()
        return lista_produtos
    else:
        Utils.limpar_tela()
        print("Saindo do sistema...")
        exit()
    
    
