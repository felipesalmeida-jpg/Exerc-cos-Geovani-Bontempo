from app import processar_envio


def test_processar_envio_chama_enviar_mensagem_externa_corretamente(mocker):
    # Substitui a função enviar_mensagem_externa por um Stub/Spy
    mock_enviar = mocker.patch('app.enviar_mensagem_externa')
    mock_enviar.return_value = "Mensagem enviada para joao@teste.com: Ola!"

    resultado = processar_envio("joao@teste.com", "Ola!")

    # Verifica se foi chamada exatamente uma vez com os argumentos corretos
    mock_enviar.assert_called_once_with("joao@teste.com", "Ola!")

    # Verifica se processar_envio retorna o valor configurado no Stub
    assert resultado == "Mensagem enviada para joao@teste.com: Ola!"
