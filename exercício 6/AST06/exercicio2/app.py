from abc import ABC, abstractmethod
from typing import Optional


class IRepositorioUsuarios(ABC):
    """Interface (contrato) para qualquer repositorio de usuarios."""

    @abstractmethod
    def adicionar_usuario(self, nome: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def buscar_usuario(self, nome: str) -> Optional[str]:
        raise NotImplementedError


class RepositorioUsuariosFake(IRepositorioUsuarios):
    """
    Implementacao em memoria do repositorio, usada nos testes
    para nao depender de um banco de dados real.
    """

    def __init__(self):
        self._usuarios = []

    def adicionar_usuario(self, nome: str) -> None:
        self._usuarios.append(nome)

    def buscar_usuario(self, nome: str) -> Optional[str]:
        if nome in self._usuarios:
            return nome
        return None


class GerenciadorUsuarios:
    """
    Classe de negocio que depende da interface IRepositorioUsuarios,
    nao de uma implementacao concreta (inversao de dependencia).
    """

    def __init__(self, repositorio: IRepositorioUsuarios):
        self.repositorio = repositorio

    def registrar_usuario(self, nome: str) -> None:
        self.repositorio.adicionar_usuario(nome)

    def encontrar_usuario(self, nome: str) -> Optional[str]:
        return self.repositorio.buscar_usuario(nome)
