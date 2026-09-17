import pytest
from pathlib import Path
from selenium import webdriver

@pytest.fixture
def navegador():
    # Cuida do ciclo de vida do navegador — abre o Chrome, entrega para o teste rodar (yield) e fecha a janela no final (driver.quit).
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_verificar_titulo_do_playground(navegador):
    # # Executa a validação — descobre o caminho do playground.html, abre o arquivo no Chrome e checa se o título da aba é exatamente "Playground Selenium" (assert).
    pasta_atual = Path(__file__).parent.absolute()
    caminho_html = (pasta_atual / "playground.html").as_uri() # O código utiliza um caminho para um arquivo HTML local na mesma pasta que o script de teste, em vez de acessar um site na Internet. O prefixo `file://` indica ao navegador para abrir um arquivo local.
    
    navegador.get(caminho_html)
    
    assert navegador.title == "Playground Selenium"

