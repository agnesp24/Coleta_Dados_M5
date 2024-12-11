import requests
from bs4 import BeautifulSoup

#Exibir o texto do site
#print(extracao.text.strip()) #Strip remove os espaços em branco


#Função para filtrar a exibição pela tag
def filtro_tags():
    url = "https://wiki.python.org.br/AprendaMais"
    requisicao = requests.get(url)
    extracao = BeautifulSoup(requisicao.text, "html.parser")

    conta_h2 = 0
    conta_p = 0

    for linha_texto in extracao.find_all(["h2","p"]):
        if linha_texto.name == "h2":
            titulo = (linha_texto.text.strip())
            conta_h2 += 1
            print("Título: ", conta_h2, titulo)
        elif linha_texto.name == "p":
            conta_p += 1
            paragrafo = (linha_texto.text.strip())
            print(conta_p, paragrafo)


#Função: Extraindo links(a) de dentro de parágrafos(p), que estão dentro de títulos(h2).
def extrair_links():
    url = "https://wiki.python.org.br/AprendaMais"
    requisicao = requests.get(url)
    extracao = BeautifulSoup(requisicao.text, "html.parser")

    for titulo in extracao.find_all("h2"):
        print("Título: ", titulo.text.strip())
        for link in titulo.find_next_siblings("p"):
            for a in link.find_all("a", href=True):
                print("Link: ", a.text.strip(), "| URL: ", a["href"])

#Módulo principal
extrair_links()