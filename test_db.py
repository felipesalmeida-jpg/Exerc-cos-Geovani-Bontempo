import os

# ===== Exercicio 1: Gerenciamento de Recursos com yield =====
def test_escrita_log(log_file):
    with open(log_file, "w") as f:
        f.write("Teste de log")
    assert os.path.exists(log_file)


# ===== Exercicio 2: Escopos, autouse e conftest.py =====
def test_db_conexao_1(db_connection):
    assert db_connection == "Conexao Global Estabelecida"


def test_db_conexao_2(db_connection):
    assert db_connection == "Conexao Global Estabelecida"


# ===== Exercicio 3: Parametrizcao Dinamica de Fixtures =====
def test_access_control(user_data):
    if user_data["role"] == "guest":
        assert user_data["access"] is False
    else:
        assert user_data["access"] is True


# ===== Exercicio 4: Desafio de Refatoracao e Isolamento =====
def test_processamento_de_dados(app_env):
    banco_falso = ["item1", "item2"]

    # Execucao
    banco_falso.append("item3")

    # Assercoes
    import os
    assert os.environ["APP_ENV"] == "testing"
    assert len(banco_falso) == 3
    # Nao precisa de teardown manual - monkeypatch (dentro da fixture app_env)
    # remove o APP_ENV automaticamente ao final do teste, mesmo se falhar.
