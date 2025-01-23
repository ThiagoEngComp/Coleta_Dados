import requests
from bs4 import BeautifulSoup
import pandas as pd

# Request usando a biblioteca requests
print('Request: ')
response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
print(response.text[:600])  # Exibe os primeiros 600 caracteres da resposta

# Usando BeautifulSoup para analisar o conteúdo HTML
print('BeautifulSoup')
soup = BeautifulSoup(response.text, features='html.parser')
print(soup.prettify()[:1000])  # Exibe os primeiros 1000 caracteres do HTML formatado

# Tentativa de ler a tabela diretamente com pandas
print('Pandas: ')
url_dados = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
print(url_dados[0].head(10))  # Exibe as 10 primeiras linhas da primeira tabela encontrada
