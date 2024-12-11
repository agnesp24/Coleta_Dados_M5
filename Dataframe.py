import pandas
from numpy.ma.core import less_equal


def lista():
    #Lista -- coleção ordenada de elementos que podem ser de qualquer tipo.
    lista_nomes = ['agnes', 'beatriz', 'do', 'prado']
    print("Lista de nomes: \n ", lista_nomes)
    print('Primeiro nome da lista: \n', lista_nomes[0])

def dicionario():
    #Dicionário -- estrutura composta por pares de chave-valor
    cadastro = {
        'nome': 'agnes',
        'idade': 23
    }
    print('Cadastro: \n', cadastro)
    print('Nome:', cadastro.get('nome'))

def lista_dicionario():
    dados = [
        {'nome': 'agnes', 'idade': 23},
        {'nome': 'kawan', 'idade': 23},
        {'nome': 'isa', 'idade': 13}
    ]
    print(dados)

def dataframe():
    dados = [
        {'nome': 'agnes', 'idade': 23},
        {'nome': 'kawan', 'idade': 23},
        {'nome': 'isa', 'idade': 13}
    ]
    #Dataframe é utilizada para lidar com dados tabulares.
    dataf = pandas.DataFrame(dados)
    print('Dataframe: \n', dataf)

    #Selecionando uma coluna
    print('\n', dataf['nome'])

    #Selecionando a primeira linha\primeiro registro
    print('\n', dataf.iloc[0])

    #Adicionar uma nova coluna
    dataf['cidade'] = ['monte mor', 'campinas', 'monte mor']
    print('\n', dataf)

    #Adicionar um novo registro
    dataf.loc[len(dataf)] = {
        'nome': 'rose',
        'idade': 50,
        'cidade': 'monte mor'
    }
    print(dataf)

    #Remover uma coluna
    dataf.drop('endereço', axis=1, inplace=True)

    #Filtrando as informações
    filtro_idade = dataf[dataf['idade'] > 30]
    print(filtro_idade)

    #Salvando o dataframe em um arquivo CSV
    dataf.to_csv('Dataframe.csv', index=False)

    #Lendo um arquivo CSV em um dataframe
    ler_dataf = pandas.read_csv('Dataframe.csv')
    print(ler_dataf)

#lista()
#dicionario()
#lista_dicionario()
#dataframe()