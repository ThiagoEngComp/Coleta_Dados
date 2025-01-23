import pandas as pd
import random
from faker import Faker

faker = Faker('pt_BR')

dados_pessoas = []

for _ in range(1026):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime('%d/%m/%Y')
    endereco = faker.address()
    estado = faker.estado()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data': data,
        'endereco': endereco,
        'estado': estado,
        'pais': pais
    }

    dados_pessoas.append(pessoa)

df_pessoas = pd.DataFrame(dados_pessoas)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

# Salvando o DataFrame em um arquivo CSV
df_pessoas.to_csv('clientes.csv', index=False, encoding='utf-8')

print("Arquivo 'clientes.csv' gerado com sucesso!")
