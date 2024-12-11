from time import strftime
import pandas
import random
from faker import Faker

#Função para gerar dados fictícios
def gerar_dados():
    faker = Faker('pt-br') #Setando a linguagem dos dados

    dados = [] #Lista vazia

    for _ in range(10):
        nome = faker.name()
        cpf = faker.cpf()
        idade = random.randint(18,60)
        data = faker.date_of_birth(minimum_age=idade, maximum_age=idade),strftime('%d/%m/%y') #A data poderia ser yyyy-mm-dd/dd--mm-yyyy
        endereco = faker.address()
        estado = faker.state()
        pais = 'Brasil'

        pessoa = {
            'nome': nome,
            'CPF': cpf,
            'idade': idade,
            'data': data,
            'endereço': endereco,
            'estado': estado,
            'pais': pais
        }

        dados.append(pessoa)

    #Criação do dataframe (dados em forma de tabela)
    dataf_pessoas = pandas.DataFrame(dados)

    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_colwidth', None)
    pandas.set_option('display.width', None)

    print(dataf_pessoas)

    # print(dataf_pessoas.to_string())

    dataf_pessoas.to_csv("Dados_ficticios.csv")

gerar_dados()