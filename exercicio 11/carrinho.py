def criar_carrinho():
    """Cria um carrinho vazio representado por um dicionário."""
    return {"total": 0, "itens": 0}


def adicionar_produto(carrinho, quantidade_desejada, estoque_disponivel, preco_unitario):
    """Adiciona produto ao carrinho se houver estoque suficiente."""
    if quantidade_desejada <= estoque_disponivel:
        carrinho["itens"] += quantidade_desejada
        carrinho["total"] += quantidade_desejada * preco_unitario
    else:
        raise ValueError("Estoque insuficiente")
