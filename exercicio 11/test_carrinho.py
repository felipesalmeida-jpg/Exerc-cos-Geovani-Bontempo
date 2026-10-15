from pytest_bdd import scenarios, given, when, then, parsers
from carrinho import criar_carrinho, adicionar_produto

# Conecta o arquivo .feature aos testes
scenarios("carrinho.feature")


# DADO (contexto inicial)
@given("que o carrinho está vazio", target_fixture="estado_do_carrinho")
def carrinho_vazio():
    return criar_carrinho()


# QUANDO (ação)
@when(
    parsers.parse(
        "o cliente adiciona {quantidade:d} unidades de um produto "
        "com estoque de {estoque:d} e preço de {preco:d} reais"
    )
)
def cliente_adiciona(estado_do_carrinho, quantidade, estoque, preco):
    try:
        adicionar_produto(estado_do_carrinho, quantidade, estoque, preco)
    except ValueError as e:
        # Guarda o erro no estado para validar no @then
        estado_do_carrinho["erro"] = str(e)


# ENTÃO (validações)
@then(parsers.parse("o total do carrinho deve ser {total_esperado:d} reais"))
def verifica_total(estado_do_carrinho, total_esperado):
    assert estado_do_carrinho["total"] == total_esperado


@then(parsers.parse("o carrinho deve ter {itens_esperados:d} itens"))
def verifica_itens(estado_do_carrinho, itens_esperados):
    assert estado_do_carrinho["itens"] == itens_esperados


@then(parsers.parse('o sistema deve exibir o erro "{mensagem}"'))
def verifica_erro(estado_do_carrinho, mensagem):
    assert estado_do_carrinho.get("erro") == mensagem
