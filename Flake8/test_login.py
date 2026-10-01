MENSAGEM_SUCESSO = (
    "Iniciando o processo de login no sistema com credenciais validas "
    "e aguardando o tempo de resposta do servidor..."
)


def realizar_login(usuario, senha, forcar_erro):
    falhas = (
        (not usuario, "Usuario invalido"),
        (senha is None, "Senha vazia"),
        (forcar_erro, "Erro forcado"),
    )
    for falhou, mensagem in falhas:
        if falhou:
            print(mensagem)
            return False

    print(MENSAGEM_SUCESSO)
    return True


def test_verificar_login_valido():
    token_sessao = "abc123xyz"  # noqa: F841
    assert realizar_login(True, "123456", False)
