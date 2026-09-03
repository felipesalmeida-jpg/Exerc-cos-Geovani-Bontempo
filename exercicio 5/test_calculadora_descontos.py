import pytest
from calculadora_descontos import calcular_valor_final


class TestCenarioBasico:
    def test_dez_por_cento_de_100(self):
        assert calcular_valor_final(100, 10) == 90

    def test_sem_desconto(self):
        assert calcular_valor_final(50, 0) == 50

    def test_desconto_total(self):
        assert calcular_valor_final(100, 100) == 0

    def test_valor_com_quebra(self):
        assert calcular_valor_final(80, 15) == 68


class TestPercentualInvalido:
    def test_percentual_maior_que_100(self):
        with pytest.raises(ValueError):
            calcular_valor_final(100, 101)

    def test_percentual_negativo(self):
        with pytest.raises(ValueError):
            calcular_valor_final(100, -1)

    @pytest.mark.parametrize("percentual", [-10, -0.5, 101, 150])
    def test_varias_entradas_invalidas(self, percentual):
        with pytest.raises(ValueError):
            calcular_valor_final(200, percentual)


class TestDescontoMaiorQueValor:
    def test_final_nunca_negativo(self):
        assert calcular_valor_final(100, 100) == 0
