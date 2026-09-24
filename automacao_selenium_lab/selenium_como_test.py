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
    pasta_atual = Path(__file__).parent.absolute()
    caminho_html = (pasta_atual / "playground.html").as_uri()
    
    navegador.get(caminho_html)
    
    assert navegador.title == "Playground Selenium"