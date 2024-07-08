from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

Service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service,options=options)

# Entrando no site
url = 'https://www.trt.net.tr/portuguese/covid19'
driver.get(url)

pais = ['China','Cuba','Laos','Vietnã','Venezuela']
#Pesquisar na lista o pais 
for i in pais:
    driver.find_element(By.XPATH,'//*[@id="filterField"]').send_keys(i)
    table_html = driver.find_element(By.ID, 'table').get_attribute('outerHTML')
    df = pd.read_html(table_html)[0]
    df.to_csv('tabela_extraida.csv', index=False)
    print(df)
    driver.find_element(By.XPATH,'//*[@id="filterField"]').clear()