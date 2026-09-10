#Calculadora de Descontos

def calcular_valor_final(valor_original, percentual_desconto):
    if not (0 <= percentual_desconto <= 100):
        raise ValueError("percentual_desconto deve estar entre 0 e 100")

    desconto = valor_original * (percentual_desconto / 100)
    valor_final = valor_original - desconto

    return max(valor_final, 0)
