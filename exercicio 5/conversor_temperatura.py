def _validar_entrada(valor):
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise TypeError("a entrada deve ser numérica")


def celsius_para_fahrenheit(celsius):
    _validar_entrada(celsius)
    return round(celsius * 9 / 5 + 32, 2)


def fahrenheit_para_celsius(fahrenheit):
    _validar_entrada(fahrenheit)
    return round((fahrenheit - 32) * 5 / 9, 2)
