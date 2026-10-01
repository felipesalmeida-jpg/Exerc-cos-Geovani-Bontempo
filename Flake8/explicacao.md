# Explicação

**E711/E712:** comparar com `None`, `True` ou `False` usando `==`/`!=` é má prática porque `==` chama `__eq__`, que pode ser sobrescrito e dar resultado inesperado (e `1 == True` é verdadeiro). `None` é singleton e deve ser checado com identidade (`is None`/`is not None`); booleanos devem ser testados direto (`if usuario:`, `if not forcar_erro:`), que é a forma Pythonic.

**Plugin de Pytest:** o plugin correto se chama `flake8-pytest-style` (o nome `flake8-pyteststyle` do enunciado não existe). Ele checa convenções do pytest (prefixo `PT`), como parênteses em fixtures, `pytest.raises` com `match` e asserts compostos. No `assert ... == True`, a correção é o assert direto (`assert realizar_login(...)`), pois já é um teste de valor verdadeiro. `# noqa: F841` ignora o erro só em uma linha, sem mexer no `.flake8`.
