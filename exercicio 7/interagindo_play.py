import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

print("Iniciando a Aula Prática de Selenium... preparando ambiente\n")

caminho_arquivo = f"file://{Path(__file__).parent.absolute()}/playground.html"
driver = webdriver.Chrome() # Inicia uma nova instância do Google Chrome controlada pelo Selenium
driver.get(caminho_arquivo) # Carrega o conteúdo do arquivo HTML
driver.maximize_window() # Abre a janela do Chrome em tela cheia

acoes_avancadas = ActionChains(driver) # Instanciação de ActionChains
time.sleep(2)

try:
    print("Executando clique simples...")
    caixa_clique = driver.find_element(By.ID, 'caixa-clique') # Vasculha o código HTML da página procurando por um elemento que tenha o atributo id="caixa-clique"
    caixa_clique.click() # Simula um clique físico do mouse em cima do elemento
    time.sleep(2)

    print("Executando duplo clique...")
    caixa_duplo = driver.find_element(By.ID, 'caixa-duplo')
    acoes_avancadas.double_click(caixa_duplo).perform() # Prepara o comando de "clicar duas vezes rapidamente", `perform()` é o gatilho da ação
    time.sleep(2)

    print("Executando clique com o botão direito...")
    caixa_direito = driver.find_element(By.ID, 'caixa-direito')
    acoes_avancadas.context_click(caixa_direito).perform()
    time.sleep(2)

    print("Limpando texto e digitando com o teclado...")
    area_teclado = driver.find_element(By.ID, 'area-teclado')
    area_teclado.click() # Clica na caixa de texto para focar nela
    
    acoes_avancadas\
        .key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)\
        .send_keys(Keys.BACKSPACE)\
        .perform() # Primeira linha "aperta" a tecla Control (Ctrl) e a mantém pressionada, toca na tecla "A" e finalmente solta a tecla. A segunda linha apaga o conteúdo.
    
    time.sleep(1)
    
    area_teclado.send_keys("Automação concluída com sucesso!")
    time.sleep(3)

    print("\n✅ Todas as ações foram executadas com sucesso.")

finally:
    print("Encerrando o navegador...")
    driver.quit() # Fecha tudo e mata o processo do driver (diferente do `driver.close()` que fecha apenas a janela/aba que está em foco no momento)
