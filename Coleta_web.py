import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python"
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, "html.parser")

#Exibir o texto do site
#print(extracao.text.strip()) #Strip remove os espaços em branco


#Filtrar a exibição pela tag

conta_h2 = 0

for linha_texto in extracao.find_all("h2"):
    if (linha_texto.name == "h2"):
        titulo = (linha_texto.text.strip())
        conta_h2 += 1
    print(conta_h2, titulo)
