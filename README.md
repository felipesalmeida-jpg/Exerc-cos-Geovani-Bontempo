# Exerc-cos-Geovani-Bontempo

Para rodar um teste individual com pytest, você tem algumas opções:

Por arquivo:

python3.14 -m pytest "exercício 4/test_db.py" -s -v

Por nome do teste:

python3.14 -m pytest -s -v -k "test_escrita_log"

O filtra pelo-k

python3.14 -m pytest -s -v -k "access_control"

Isso vai rodar só os testes que contêm "access_control" no nome (no caso, as 3 variações parametrizadas do Exercício 3).

Por teste exato (inclusive um parâmetro específico):

python3.14 -m pytest -s -v "exercício 4/test_db.py::test_access_control[user_data0]"

O 'user_dat

Resumo das opções mais úteis:

'-k "não
-v — mostra cada teste com nome completo
-s — mostra os prints no console
