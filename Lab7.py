import pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

def atv1():
    url = 'https://books.toscrape.com/'
    requisicao = requests.get(url)

    # Escreve seu código abaixo
    extracao = BeautifulSoup(requisicao.text, 'html.parser')
    print(extracao.prettify()[:200])

def atv2():
    url = 'https://books.toscrape.com/'
    requisicao = requests.get(url)
    requisicao.encoding = 'utf-8'

    # Escreve seu código abaixo
    extracao = BeautifulSoup(requisicao.text, 'html.parser')

    for linha_texto in extracao.find_all('h3'):
        titulo = linha_texto.text.strip()
        print('Título: ', titulo)

def atv21():
    url = 'https://books.toscrape.com/'
    requisicao = requests.get(url)
    requisicao.encoding = 'utf-8'

    # Escreve seu código abaixo
    extracao = BeautifulSoup(requisicao.text, 'html.parser')

    conta_livros = 0
    catalogo = []

    for resposta in extracao.find_all('article', class_='product_pod'):
        livro = {}
        for titulo in resposta.find_all('h3'):
            titulo = titulo.text.strip()
            livro['Título: '] = titulo
        for preco in resposta.find_all('p', class_='price_color'):
            preco = preco.text.strip()
            livro['Preço: '] = preco
            catalogo.append(livro)
            conta_livros += 1

    # print(catalogo)
    # print('Total de livros: ', conta_livros)

    dataf = pandas.DataFrame(catalogo)
    print(dataf)

#atv2()
atv21()
