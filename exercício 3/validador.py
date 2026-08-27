def validar_acesso(idade, possui_convite, vip=False):
    if idade < 0:
        raise ValueError("Idade inválida")
    if vip:
        return "Acesso VIP Liberado"
    elif idade >= 18 and possui_convite:
        return "Acesso Permitido"
    elif idade >= 18 and not possui_convite:
        return "Comprar Ingressos"
    else:
        return "Acesso Negado: Menor de Idade"