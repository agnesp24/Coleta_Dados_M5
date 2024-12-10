import requests

def envio_arquivos():
    caminho = r"C:\Users\agnes\Downloads\produtos_informatica.xlsx" #O caminho de onde os arquivos serão enviados.

    #Request para enviar o arquivo usando POST, que envia.
    requisicao_envio = requests.post("https://file.io", files={"file": open(caminho, "rb")}) #Tipo RB = R read e B de binary. Serve para ficar mais leve o arquivo.
    requisicao_saida = requisicao_envio.json()

    print(requisicao_saida)
    url = requisicao_saida["link"]
    print("Arquivo enviado. Link para acesso: ", url)


def receber_arquivos(file_url):
    #Pegar o arquivo
    requisicao_receber = requests.get(file_url)

    #Salvar o arquivo
    if requisicao_receber.ok:
        with open("arquivo_baixado.xlsx", 'wb') as file:
            file.write(requisicao_receber.content)
        print("Baixado")
    else:
        print("No")

def envio_seguro():
    caminho = r"C:\Users\agnes\Downloads\produtos_informatica.xlsx"
    chave_acesso = 'NMJDVNK.0KYR25Q-1DWM3JW-MQDPN8J-R34HDES' #API KEY

    #Envio do arquivo
    requisicao_envio = requests.post('https://file.io', files={'file': open(caminho, 'rb')}, headers={"Authorization": chave_acesso})
    requisicao_saida = requisicao_envio.json()

    print(requisicao_saida)
    url = requisicao_saida["link"]
    print("Arquivo enviado. Link para acesso: ", url)

#envio_arquivos()
#receber_arquivos("https://file.io/HfNb0GwpQO3O")
# envio_seguro()
