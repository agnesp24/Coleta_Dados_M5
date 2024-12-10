# Importação de pacotes para fazer a coleta de dados. Vamos importar o REQUESTS, que faz requisições HTTP.
import requests # Se está cinza, a biblioteca não está sendo utilizada.
from bs4 import BeautifulSoup # Importação apenas de uma classe do pacote BS4.
import pandas

# Módulo
response = requests.get("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/")
print(response.text[:600]) # SLICING -- [:600] -- Seleção de quantos caracteres queremos que retorne

# Beautiful Soup -- Classe (estrutura de dados, tipo de dado) do módulo que possui várias características que podemos estruturar.
soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify()[:1000])

# Web scrapping
print("\nUtilizando o pandas")
url_dados = pandas.read_html("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/")
print(url_dados[2].head(5))