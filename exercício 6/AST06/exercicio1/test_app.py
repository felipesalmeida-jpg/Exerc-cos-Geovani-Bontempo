from app import processar_envio


def test_processar_envio_chama_enviar_mensagem_externa_corretamente(mocker):
    # Stub/Spy: substitui a dependencia externa por um mock controlado,
    # configurado com um retorno fixo
    mock_enviar = mocker.patch(
        "app.enviar_mensagem_externa",
        return_value="Mensagem enviada para cliente@teste.com: Ola, mundo!",
    )

    resultado = processar_envio("cliente@teste.com", "Ola, mundo!")

    # Verifica que a funcao externa foi chamada exatamente uma vez,
    # com os argumentos corretos
    mock_enviar.assert_called_once_with("cliente@teste.com", "Ola, mundo!")

    # Verifica que processar_envio repassa o retorno fixo do stub
    assert resultado == "Mensagem enviada para cliente@teste.com: Ola, mundo!"
