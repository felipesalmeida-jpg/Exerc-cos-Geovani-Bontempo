def enviar_mensagem_externa(destinatario: str, conteudo: str) -> str:
    """
    Simula a dependencia externa (ex: API de e-mail/SMS) que
    nao queremos chamar de verdade nos testes.
    """
    return f"Mensagem enviada para {destinatario}: {conteudo}"


def processar_envio(destinatario: str, texto: str) -> str:
    """
    Processa o envio, delegando a comunicacao externa para
    enviar_mensagem_externa e repassando o resultado.
    """
    return enviar_mensagem_externa(destinatario, texto)
