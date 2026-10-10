def aprovar_emprestimo(score_serasa: int, renda_mensal: float) -> bool:
    # Regra: Aprova se o score for maior ou igual a 700 OU a renda for maior que 5000.00
    if score_serasa >= 700 or renda_mensal > 5000.00:
        return True
    return False
