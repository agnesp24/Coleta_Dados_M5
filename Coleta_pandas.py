import pandas

print("Utilizando o pandas")
url_dados = pandas.read_html("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/")
print(url_dados[2].head(5))