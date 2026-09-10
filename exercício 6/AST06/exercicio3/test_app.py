from unittest.mock import MagicMock, call
from app import ProcessadorDeAcoes


def test_executar_processo_chama_metodos_na_ordem_correta(mocker):
    # Mock com a mesma "spec" da classe real, garantindo que so
    # metodos que realmente existem em ProcessadorDeAcoes podem ser chamados
    mock_processador = MagicMock(spec=ProcessadorDeAcoes)
    # Configura o retorno como o bool literal True (nao um MagicMock).
    # Sem isso, o "if" dentro de executar_processo forca uma chamada
    # implicita a .__bool__() no mock, que se insere entre as duas
    # chamadas esperadas e quebra a sequencia exata do assert_has_calls.
    mock_processador.validar_dados.return_value = True

    dados = {"id": 1, "valor": "teste"}

    # Chama o metodo REAL de ProcessadorDeAcoes, mas passando o mock
    # no lugar de self -- assim conseguimos espionar as chamadas
    # internas a validar_dados/salvar_dados
    resultado = ProcessadorDeAcoes.executar_processo(mock_processador, dados)

    # Verifica a ORDEM exata das chamadas e os parametros passados
    roteiro_esperado = [
        call.validar_dados(dados),
        call.salvar_dados(dados),
    ]
    mock_processador.assert_has_calls(roteiro_esperado, any_order=False)

    # Verifica se a mensagem de sucesso esperada foi retornada
    assert resultado == "Processo executado com sucesso"
