from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Parte 1: Configuração Inicial, Headless e Segurança de Rede
options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

try:
    # Parte 2: Orquestração de Abas
    # Aba 0
    driver.get("https://the-internet.herokuapp.com/dropdown")
    
    # Aba 1
    driver.execute_script("window.open('https://the-internet.herokuapp.com/dynamic_loading/2', '_blank');")
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    
    # Aba 2
    driver.execute_script("window.open('https://pt.wikipedia.org', '_blank');")
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(3))
    
    handles = driver.window_handles

    # Parte 3: Interação com Dropdowns (Voltando à Aba 0)
    driver.switch_to.window(handles[0])
    dropdown_element = driver.find_element(By.ID, "dropdown")
    select = Select(dropdown_element)
    select.select_by_visible_text("Option 1")
    valor_selecionado = select.first_selected_option.get_attribute("value")
    print(f"[Aba 0] Valor selecionado no dropdown: {valor_selecionado}")

    # Parte 4: Sincronização Dinâmica (Aba 1)
    driver.switch_to.window(handles[1])
    botao_start = driver.find_element(By.CSS_SELECTOR, "#start button")
    botao_start.click()
    
    # Espera Explícita para o elemento de carregamento lento
    elemento_finish = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    print(f"[Aba 1] Texto de carregamento concluído: {elemento_finish.text}")

    # Parte 5: Extração de Dados e Evidências (Aba 2)
    driver.switch_to.window(handles[2])
    barra_pesquisa = driver.find_element(By.NAME, "search")
    barra_pesquisa.send_keys("Automação")
    
    # Localizando o link "Artigo destacado" no menu lateral da Wikipedia
    link_lateral = driver.find_element(By.PARTIAL_LINK_TEXT, "Página principal")
    texto_link = link_lateral.text
    destino_link = link_lateral.get_attribute("href")
    
    print(f"[Aba 2] Texto do link lateral: {texto_link}")
    print(f"[Aba 2] Destino do link (href): {destino_link}")
    
    # Tirando o screenshot
    driver.save_screenshot("evidencia_wiki.png")
    print("\nScreenshot 'evidencia_wiki.png' salvo com sucesso!")
finally:
    # Parte 6: Encerramento
    driver.quit()