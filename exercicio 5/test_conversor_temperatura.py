import pytest
from conversor_temperatura import celsius_para_fahrenheit, fahrenheit_para_celsius


class TestCelsiusParaFahrenheit:
    def test_zero_graus(self):
        assert celsius_para_fahrenheit(0) == 32.00

    def test_cem_graus(self):
        assert celsius_para_fahrenheit(100) == 212.00

    def test_valor_negativo(self):
        assert celsius_para_fahrenheit(-40) == -40.00

    def test_valor_com_quebra(self):
        assert celsius_para_fahrenheit(36.6) == 97.88


class TestFahrenheitParaCelsius:
    def test_trinta_e_dois(self):
        assert fahrenheit_para_celsius(32) == 0.00

    def test_duzentos_e_doze(self):
        assert fahrenheit_para_celsius(212) == 100.00

    def test_valor_negativo(self):
        assert fahrenheit_para_celsius(-40) == -40.00

    def test_valor_com_quebra(self):
        assert fahrenheit_para_celsius(98.6) == 37.00

class TestEntradaNaoNumerica:
    @pytest.mark.parametrize("entrada", ["abc", None, [10], True])
    def test_celsius_com_entrada_invalida(self, entrada):
        with pytest.raises(TypeError):
            celsius_para_fahrenheit(entrada)

    @pytest.mark.parametrize("entrada", ["quente", None, {"temp": 10}, True])
    def test_fahrenheit_com_entrada_invalida(self, entrada):
        with pytest.raises(TypeError):
            fahrenheit_para_celsius(entrada)
