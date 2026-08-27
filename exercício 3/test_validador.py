import pytest  # <--- É ESTA LINHA QUE ESTAVA FALTANDO!
from validador import validar_acesso

def test_acesso_permitido():
    resultado = validar_acesso(20, True)
    assert resultado == "Acesso Permitido"
    

def test_menor_de_idade():
    resultado = validar_acesso(15, False)
    assert resultado == "Acesso Negado: Menor de Idade"
    
# --- NOVOS TESTES PARA ATINGIR 100% DE COBERTURA (Linhas Amarelas/Vermelhas) ---

def test_idade_invalida_excecao():
    # Testa a linha 2 e 3 (Amarela e Vermelha)
    with pytest.raises(ValueError, match="Idade inválida"):
        validar_acesso(-1, False)

def test_acesso_vip_liberado():
    # Testa a linha 4 e 5 (Amarela e Vermelha)
    assert validar_acesso(25, False, vip=True) == "Acesso VIP Liberado"

def test_comprar_ingressos():
    # Testa a linha 8 e 9 (Amarela e Vermelha)
    assert validar_acesso(20, False, vip=False) == "Comprar Ingressos"