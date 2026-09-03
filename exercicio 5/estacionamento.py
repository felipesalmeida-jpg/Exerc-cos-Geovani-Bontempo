TARIFA_PRIMEIRA_HORA = 10.00
TARIFA_HORA_ADICIONAL = 5.00
TETO_DIARIA = 50.00


def calcular_valor_estacionamento(tempo_em_minutos):
    if tempo_em_minutos <= 0:
        raise ValueError("tempo_em_minutos deve ser maior que zero")

    valor = TARIFA_PRIMEIRA_HORA

    minutos_excedentes = tempo_em_minutos - 60
    if minutos_excedentes > 0:
        horas_adicionais = -(-minutos_excedentes // 60)  # arredonda pra cima
        valor += horas_adicionais * TARIFA_HORA_ADICIONAL

    return min(valor, TETO_DIARIA)
