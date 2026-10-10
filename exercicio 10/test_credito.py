import pytest

from credito import aprovar_emprestimo


# --- Cenários originais do desenvolvedor ---
def test_aprovacao_por_score():
    # Passa com score alto
    assert aprovar_emprestimo(850, 2000.00) is True


def test_aprovacao_por_renda():
    # Passa com renda alta
    assert aprovar_emprestimo(500, 8000.00) is True


def test_reprovacao():
    # Reprova com tudo baixo
    assert aprovar_emprestimo(300, 1500.00) is False


# --- Análise de Valor Limite: score (regra: score >= 700) ---
@pytest.mark.parametrize(
    "score, esperado",
    [
        (699, False),  # logo abaixo do limite
        (700, True),   # exatamente no limite (mata >= -> > e 700 -> 701)
        (701, True),   # logo acima do limite
    ],
)
def test_limite_score(score, esperado):
    # Renda baixa e fixa, para isolar a regra do score
    assert aprovar_emprestimo(score, 1000.00) is esperado


# --- Análise de Valor Limite: renda (regra: renda > 5000.00) ---
@pytest.mark.parametrize(
    "renda, esperado",
    [
        (4999.99, False),  # logo abaixo do limite
        (5000.00, False),  # exatamente no limite: NÃO aprova (mata > -> >=)
        (5000.01, True),   # logo acima do limite
        (5001.00, True),   # mata 5000.00 -> 5001.0
    ],
)
def test_limite_renda(renda, esperado):
    # Score baixo e fixo, para isolar a regra da renda
    assert aprovar_emprestimo(300, renda) is esperado
