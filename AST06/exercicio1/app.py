def enviar_mensagem_externa(destinatario: str, conteudo: str) -> str:
    """Simula o envio de uma mensagem por um serviço externo (e-mail/SMS)."""
    return f"Mensagem enviada para {destinatario}: {conteudo}"


def processar_envio(destinatario: str, texto: str) -> str:
    """Processa o envio de uma mensagem delegando para a dependência externa."""
    return enviar_mensagem_externa(destinatario, texto)
