import pytest
from app import GerenciadorUsuarios, RepositorioUsuariosFake


@pytest.fixture
def repositorio():
    return RepositorioUsuariosFake()


@pytest.fixture
def gerenciador(repositorio):
    return GerenciadorUsuarios(repositorio)


def test_registrar_e_encontrar_usuario(gerenciador):
    gerenciador.registrar_usuario("Felipe")

    usuario_encontrado = gerenciador.encontrar_usuario("Felipe")

    assert usuario_encontrado == "Felipe"


def test_encontrar_usuario_nao_adicionado_retorna_none(gerenciador):
    usuario_encontrado = gerenciador.encontrar_usuario("NaoExiste")

    assert usuario_encontrado is None
