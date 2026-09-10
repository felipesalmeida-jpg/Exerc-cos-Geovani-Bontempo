import pytest
from estacionamento import calcular_valor_estacionamento


class TestPrimeiraHora:
    def test_trinta_minutos(self):
        assert calcular_valor_estacionamento(30) == 10.00

    def test_sessenta_minutos_exatos(self):
        assert calcular_valor_estacionamento(60) == 10.00

    def test_um_minuto(self):
        assert calcular_valor_estacionamento(1) == 10.00


class TestHorasAdicionais:
    def test_setenta_minutos(self):
        assert calcular_valor_estacionamento(70) == 15.00

    def test_centoe_vinte_minutos(self):
        assert calcular_valor_estacionamento(120) == 15.00

    def test_centoe_oitenta_minutos(self):
        assert calcular_valor_estacionamento(180) == 20.00

    def test_duzentos_e_quarenta_e_um_minutos(self):
        assert calcular_valor_estacionamento(241) == 30.00


class TestTetoMaximo:
    def test_vinte_e_quatro_horas(self):
        assert calcular_valor_estacionamento(24 * 60) == 50.00

    def test_acima_do_teto_continua_50(self):
        assert calcular_valor_estacionamento(25 * 60) == 50.00


class TestEntradasInvalidas:
    def test_tempo_zero(self):
        with pytest.raises(ValueError):
            calcular_valor_estacionamento(0)

    @pytest.mark.parametrize("tempo", [-1, -60, -999])
    def test_tempo_negativo(self, tempo):
        with pytest.raises(ValueError):
            calcular_valor_estacionamento(tempo)
