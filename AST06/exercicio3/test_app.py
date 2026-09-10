from unittest.mock import call

from app import ProcessadorDeAcoes


def test_executar_processo_chama_metodos_na_ordem_correta(mocker):
    dados = {"id": 1, "nome": "Teste"}

    # Cria um Mock respeitando a interface da classe ProcessadorDeAcoes
    mock_processador = mocker.MagicMock(spec=ProcessadorDeAcoes)
    mock_processador.validar_dados.return_value = True
    mock_processador.salvar_dados.return_value = True

    # Chama executar_processo (código real) usando o Mock como "self",
    # assim validar_dados e salvar_dados chamados internamente são os mocks
    resultado = ProcessadorDeAcoes.executar_processo(mock_processador, dados)

    # Verifica a ordem exata das chamadas e os parâmetros passados
    roteiro_esperado = [
        call.validar_dados(dados),
        call.salvar_dados(dados),
    ]
    mock_processador.assert_has_calls(roteiro_esperado, any_order=False)

    # Verifica se a função retorna a mensagem de sucesso esperada
    assert resultado == "Processo executado com sucesso."
