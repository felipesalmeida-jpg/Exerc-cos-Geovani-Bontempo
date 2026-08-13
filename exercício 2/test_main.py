# test_main.py
import pytest

# Importando as funções e classes do nosso arquivo principal
from main import pode_dirigir, calcular_desconto, cadastrar_senha, CarrinhoDeCompras

# ==========================================
# EXERCÍCIO 1: O Verificador de Idade
# ==========================================

def test_pode_dirigir_maior_de_idade():
    # Arrange (Organizar)
    idade_usuario = 20
    resultado_esperado = True
    
    # Act (Agir)
    resultado = pode_dirigir(idade_usuario)
    
    # Assert (Afirmar)
    assert resultado is resultado_esperado

def test_nao_pode_dirigir_menor_de_idade():
    # Arrange (Organizar)
    idade_usuario = 16
    resultado_esperado = False
    
    # Act (Agir)
    resultado = pode_dirigir(idade_usuario)
    
    # Assert (Afirmar)
    assert resultado is resultado_esperado


# ==========================================
# EXERCÍCIO 2: Calculadora de Descontos
# ==========================================

def test_calcular_desconto_comum():
    # Arrange (Organizar)
    valor_produto = 100
    percentual_desconto = 10
    valor_esperado = 90.0
    
    # Act (Agir)
    resultado = calcular_desconto(valor_produto, percentual_desconto)
    
    # Assert (Afirmar)
    assert resultado == valor_esperado

def test_calcular_desconto_limite_de_seguranca():
    # Arrange (Organizar)
    valor_produto = 100
    percentual_desconto = 70  # O sistema deve forçar a ser 50%
    valor_esperado = 50.0
    
    # Act (Agir)
    resultado = calcular_desconto(valor_produto, percentual_desconto)
    
    # Assert (Afirmar)
    assert resultado == valor_esperado

def test_calcular_desconto_decimal():
    # Arrange (Organizar)
    valor_produto = 10.50
    percentual_desconto = 15  # Desconto de 1.575
    valor_esperado = 8.925    # 10.50 - 1.575
    
    # Act (Agir)
    resultado = calcular_desconto(valor_produto, percentual_desconto)
    
    # Assert (Afirmar)
    assert resultado == pytest.approx(valor_esperado)


# ==========================================
# EXERCÍCIO 3: Sistema de Cadastro de Senhas
# ==========================================

def test_cadastrar_senha_sucesso():
    # Arrange (Organizar)
    senha_valida = "minhasenha123"
    resultado_esperado = "Senha cadastrada com sucesso!"
    
    # Act (Agir)
    resultado = cadastrar_senha(senha_valida)
    
    # Assert (Afirmar)
    assert resultado == resultado_esperado

def test_cadastrar_senha_muito_curta():
    # Arrange (Organizar)
    senha_invalida = "123"
    
    # Act & Assert (Agir e Afirmar juntos devido à Exceção)
    with pytest.raises(ValueError):
        cadastrar_senha(senha_invalida)

def test_cadastrar_senha_muito_curta_mensagem_exata():
    # Arrange (Organizar)
    senha_invalida = "123"
    mensagem_esperada = "Senha muito curta"
    
    # Act (Agir)
    with pytest.raises(ValueError) as exc_info:
        cadastrar_senha(senha_invalida)
        
    # Assert (Afirmar)
    assert str(exc_info.value) == mensagem_esperada


# ==========================================
# EXERCÍCIO 4: Carrinho de Compras
# ==========================================

def test_adicionar_item():
    # Arrange (Organizar)
    carrinho = CarrinhoDeCompras()
    produto = "Notebook"
    
    # Act (Agir)
    carrinho.adicionar_item(produto)
    
    # Assert (Afirmar)
    assert produto in carrinho.listar_itens()

def test_remover_item():
    # Arrange (Organizar)
    carrinho = CarrinhoDeCompras()
    produto = "Mouse"
    carrinho.adicionar_item(produto) # Preparando o estado do carrinho
    
    # Act (Agir)
    carrinho.remover_item(produto)
    
    # Assert (Afirmar)
    assert produto not in carrinho.listar_itens()

def test_remover_item_inexistente_gera_erro():
    # Arrange (Organizar)
    carrinho = CarrinhoDeCompras()
    produto = "Teclado"
    mensagem_esperada = "Item não encontrado"
    
    # Act (Agir)
    with pytest.raises(ValueError) as exc_info:
        carrinho.remover_item(produto)
        
    # Assert (Afirmar)
    assert str(exc_info.value) == mensagem_esperada