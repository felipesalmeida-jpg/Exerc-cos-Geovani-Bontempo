from abc import ABC, abstractmethod
from typing import Optional


class IRepositorioUsuarios(ABC):
    @abstractmethod
    def adicionar_usuario(self, nome: str) -> None:
        ...

    @abstractmethod
    def buscar_usuario(self, nome: str) -> Optional[str]:
        ...


class RepositorioUsuariosFake(IRepositorioUsuarios):
    """Implementação Fake em memória, usada apenas para testes."""

    def __init__(self):
        self._usuarios = []

    def adicionar_usuario(self, nome: str) -> None:
        self._usuarios.append(nome)

    def buscar_usuario(self, nome: str) -> Optional[str]:
        for usuario in self._usuarios:
            if usuario == nome:
                return usuario
        return None


class GerenciadorUsuarios:
    def __init__(self, repositorio: IRepositorioUsuarios):
        self._repositorio = repositorio

    def registrar_usuario(self, nome: str) -> None:
        self._repositorio.adicionar_usuario(nome)

    def encontrar_usuario(self, nome: str) -> Optional[str]:
        return self._repositorio.buscar_usuario(nome)
