"""
AST07 - Automação e Validação de Interface com Selenium e Pytest

Suíte de testes E2E para a página local portal.html.
Execução: pytest test_portal.py -v
"""
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Caminho absoluto para a página alvo, independente de onde o pytest roda
CAMINHO_PORTAL = Path(__file__).parent.resolve() / "portal.html"


@pytest.fixture
def navegador():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless=new")      # ← remover esta linha
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(CAMINHO_PORTAL.as_uri())  # file:///caminho/absoluto/portal.html
        yield driver
    finally:
        driver.quit()


# ------------------------------------------------------------------
# Cenário 1: Validação de Título e Formulário Simples
# ------------------------------------------------------------------
def test_preencher_formulario(navegador):
    # Valida o título da aba/página
    assert navegador.title == "Portal do Colaborador"

    # Preenche os campos do formulário
    campo_nome = navegador.find_element(By.ID, "nome_usuario")
    campo_email = navegador.find_element(By.ID, "email")
    campo_nome.send_keys("Felipe Santos")
    campo_email.send_keys("felipe.santos@empresa.com.br")

    # Clica no botão de envio
    navegador.find_element(By.ID, "btn-enviar").click()

    # Valida que a mensagem de sucesso ficou visível na tela
    mensagem = navegador.find_element(By.ID, "msg-sucesso")
    assert mensagem.is_displayed(), "A mensagem de sucesso deveria estar visível"
    assert mensagem.text == "Dados enviados com sucesso!"


# ------------------------------------------------------------------
# Cenário 2: Ações Avançadas de Mouse (duplo clique e clique direito)
# ------------------------------------------------------------------
def test_acoes_avancadas_mouse(navegador):
    acoes = ActionChains(navegador)

    # Duplo clique no botão "Duplo clique para Autorizar"
    btn_duplo = navegador.find_element(By.ID, "btn-duplo")
    acoes.double_click(btn_duplo).perform()
    assert btn_duplo.text == "Autorizado!"

    # Clique com o botão direito no botão "Clique direito para Opções"
    btn_direito = navegador.find_element(By.ID, "btn-direito")
    acoes.context_click(btn_direito).perform()
    assert btn_direito.text == "Menu Aberto!"


# ------------------------------------------------------------------
# Cenário 3: Ações Avançadas de Teclado (selecionar tudo e apagar)
# ------------------------------------------------------------------
def test_acoes_teclado(navegador):
    textarea = navegador.find_element(By.ID, "obs")

    # Seleciona todo o texto do textarea (CTRL + A) e apaga (BACKSPACE)
    ActionChains(navegador) \
        .click(textarea) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.BACKSPACE) \
        .perform()

    # Digita o novo texto
    novo_texto = "Teste automatizado finalizado."
    textarea.send_keys(novo_texto)

    # Valida o valor atual do campo
    assert textarea.get_attribute("value") == novo_texto
