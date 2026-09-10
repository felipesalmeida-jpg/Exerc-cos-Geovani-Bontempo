import pytest

from app import GerenciadorUsuarios, RepositorioUsuariosFake


@pytest.fixture
def repositorio_fake():
    return RepositorioUsuariosFake()


@pytest.fixture
def gerenciador(repositorio_fake):
    return GerenciadorUsuarios(repositorio_fake)


def test_registrar_e_encontrar_usuario(gerenciador):
    gerenciador.registrar_usuario("Felipe")

    resultado = gerenciador.encontrar_usuario("Felipe")

    assert resultado == "Felipe"


def test_encontrar_usuario_nao_adicionado_retorna_none(gerenciador):
    resultado = gerenciador.encontrar_usuario("Inexistente")

    assert resultado is None
