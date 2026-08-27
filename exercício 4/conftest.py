import os
import pytest


# ===== Exercicio 1: Fixture com yield e teardown =====
@pytest.fixture
def log_file():
    caminho = "test_log.txt"
    yield caminho
    if os.path.exists(caminho):
        os.remove(caminho)


# ===== Exercicio 2: Escopos e autouse =====
@pytest.fixture(scope="session")
def db_connection():
    return "Conexao Global Estabelecida"


@pytest.fixture(autouse=True)
def clean_cache():
    print("Cache limpo antes do teste")


# ===== Exercicio 3: Parametrizacao dinamica de fixtures =====
@pytest.fixture(params=[
    {"role": "admin", "access": True},
    {"role": "editor", "access": True},
    {"role": "guest", "access": False},
])
def user_data(request):
    return request.param


# ===== Exercicio 4: Refatoracao com monkeypatch =====
@pytest.fixture
def app_env(monkeypatch):
    monkeypatch.setenv("APP_ENV", "testing")
    yield "testing"
    # monkeypatch restaura automaticamente no teardown — nada manual
