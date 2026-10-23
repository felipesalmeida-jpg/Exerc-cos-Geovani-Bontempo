# Exercícios de Testes e Qualidade de Software

[![CI - Exercicio 12](https://github.com/felipesalmeida-jpg/Exerc-cos-Geovani-Bontempo/actions/workflows/ci-exercicio-12.yml/badge.svg)](https://github.com/felipesalmeida-jpg/Exerc-cos-Geovani-Bontempo/actions/workflows/ci-exercicio-12.yml)

Repositório com as atividades práticas da disciplina de testes e qualidade de software (ADS), em Python. Cada pasta é um exercício independente.

## Exercícios

| Pasta | Tema | O que tem |
|---|---|---|
| `exercício 1` | Projeto de casos de teste | Enunciado em PDF (carrinho de e-commerce: frete e cupom) e planilha de casos de teste |
| `exercício 2` | Fundamentos do pytest | Testes no padrão AAA para idade, desconto, senha e carrinho de compras |
| `exercício 3` | Cobertura de código | `validar_acesso` testada até 100% de cobertura, com relatório em `htmlcov/` e respostas em `.docx` |
| `exercício 4` | Fixtures | `yield` com teardown, escopo `session`, `autouse`, fixtures parametrizadas e `monkeypatch` |
| `exercicio 5` | Testes unitários | Conversor de temperatura, calculadora de descontos e estacionamento |
| `exercício 6` | Mocks, stubs e fakes | Três subexercícios com `pytest-mock` e `MagicMock`: stub/spy, repositório fake e verificação da ordem das chamadas |
| `exercicio 7` | Selenium com pytest | Interações (clique, duplo clique, botão direito, teclado) e testes E2E da página `portal.html` |
| `exercicio 8` | Robô de auditoria | Selenium com várias abas, dropdown, esperas explícitas, modo headless e screenshot |
| `exercicio 9` | Qualidade de código | `flake8` com `flake8-pytest-style`, configuração em `.flake8` e explicação das regras |
| `exercicio 10` | Teste de mutação | `mutmut` e análise de valor limite em `aprovar_emprestimo` |
| `exercicio 11` | BDD | `pytest-bdd` com Gherkin em português para o carrinho de compras |
| `exercicio 12` | Integração contínua | API FastAPI com pipeline no GitHub Actions (matrix de versões e teste de integração) |

> Os nomes das pastas misturam grafia com e sem acento (`exercício 1` a `4` e `6`, `exercicio 5` e `7` a `12`). Use o nome exato nos comandos, sempre entre aspas.

## Requisitos

- Python 3.10 ou superior (desenvolvido com 3.14)
- Google Chrome, para os exercícios 7 e 8
- Internet, para o exercício 8 (acessa `the-internet.herokuapp.com` e `pt.wikipedia.org`)

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows (PowerShell)
pip install -r requirements.txt
pip install pytest-cov pytest-bdd mutmut
```

O `requirements.txt` da raiz cobre pytest, pytest-mock, Selenium e flake8. `pytest-cov` (exercício 3), `pytest-bdd` (exercício 11) e `mutmut` (exercício 10) são instalados à parte. O exercício 12 tem o seu próprio `requirements.txt`, dentro da pasta.

## Como rodar os testes

Rode **uma pasta por vez**. Os exercícios 2 e 12 têm arquivos com o mesmo nome (`test_main.py`), e rodar o pytest na raiz, sem indicar a pasta, gera erro de `import file mismatch`.

```bash
# uma pasta inteira
python -m pytest "exercício 4" -v

# um arquivo
python -m pytest "exercício 4/test_db.py" -s -v

# um teste pelo nome
python -m pytest -s -v -k "test_escrita_log"

# um teste exato, inclusive um parâmetro específico
python -m pytest -s -v "exercício 4/test_db.py::test_access_control[user_data0]"
```

Opções mais úteis:

- `-v` mostra o nome completo de cada teste
- `-s` mostra os `print` no console
- `-k "texto"` roda só os testes cujo nome contém o texto (por exemplo, `-k "access_control"` roda as 3 variações parametrizadas do exercício 4)

## Comandos específicos

Rode estes de dentro da pasta do exercício (`cd "exercício 3"`).

| Exercício | Comando |
|---|---|
| 3 | `python -m pytest --cov=validador --cov-report=html` (relatório em `htmlcov/index.html`) |
| 7 | `python -m pytest test_portal.py -v` |
| 8 | `python robo_auditoria.py` |
| 9 | `flake8 test_login.py` |
| 10 | `mutmut run` e depois `mutmut results` |
| 11 | `python -m pytest -v` |
| 12 | `python -m pytest -v` e `python -m fastapi run main.py --port 8000` |

## Integração contínua (exercício 12)

O workflow `.github/workflows/ci-exercicio-12.yml` roda a cada push ou pull request que altere a pasta `exercicio 12`:

1. Testa a API com `pytest` em Python 3.10, 3.11 e 3.12 (strategy matrix).
2. Sobe a API com `fastapi run` e faz requisições reais com `curl -f`, como teste de integração.

O workflow fica na raiz porque o GitHub só lê `.github/workflows/` no nível mais alto do repositório. Os comandos usam `working-directory` para executar dentro da pasta do exercício.

A atividade completa do exercício 12 (erro intencional, regra de proteção da `main` e Pull Requests) foi feita no repositório [ci-fastapi-ast12](https://github.com/felipesalmeida-jpg/ci-fastapi-ast12).
