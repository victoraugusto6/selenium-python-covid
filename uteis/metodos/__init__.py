from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime

# Driver
driver = webdriver.Chrome(
    "/home/victor/Documentos/Python - Projects/Selenium/selenium-python-get-text/chromedriver")

# Url
url = "https://www.coronatracker.com/"

# Abrindo página
driver.get(url)

# Aguarda 1 segundo
sleep(1)

# Datas
data_atual = datetime.today()
data_em_texto = '{}/{}/{}'.format(data_atual.day,
                                  data_atual.month, data_atual.year)

# Variáveis User
casos = driver.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
mortes = driver.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span').text
recuperados = driver.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span').text


def dados():
    print(
        f'\033[7m\n-----------  DADOS ({data_em_texto})  -----------\033[m\n')
    print(f'\033[0;31mCasos confirmados: {casos}\033[m')
    print(f'Mortes: {mortes}')
    print(f'\033[0;32mRecuperados: {recuperados}\033[m')

    # Fecha navegador
    driver.close()
