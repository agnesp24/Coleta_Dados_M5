import time
import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#Configura o Selenium para usar o Chrome no modo headless, no sandbox e disable o uso do \dev\shm\
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

#Acesse a página
url = "https://finance.yahoo.com/quote/%5EBVSP/history/"
driver.get(url)

#Aguarde alguns segundos até a página carregar
time.sleep(5)

#Extração da tabela
html = driver.page_source
tables = pandas.read_html(html)

#Feche o navegador
driver.quit()

#Checage se a extração da tabela deu certo
if tables:
    check_tb = tables[0]
    print(check_tb.head(10))
else:
    print("Nah")

