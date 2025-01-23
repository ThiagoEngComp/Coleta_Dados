from importlib.metadata import files

import requests
from bs4 import BeautifulSoup
from pyexpat import features

from requests import request


url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, features = 'html.parser')

#extrair o texto
# print(extracao.text.strip())

#Filtrar a exebição pela teg
# for linha_texto in extracao.find_all('h2'):
#     titulo = linha_texto.text.strip()
    # print('Titulo: ', titulo)

contar_titulos = 0
contar_paragrafo = 0

for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1 # Contar titulos = contar titulos = 1
    elif linha_texto.name == 'p':
        contar_paragrafo += 1

print('total titulos: ', contar_titulos)
print('total paragrafos: ', contar_paragrafo)

# for linha_texto in extracao.find_all(['h2', 'p']):
#     if linha_texto.name == 'h2':
#         titulo = linha_texto.text.strip()
#         print('Titulo \n', titulo)
#     elif linha_texto.name == 'p':
#         paragrafo = linha_texto.text.strip()
#         print('Paragrafo \n', paragrafo)

# for titulo in extracao.find_all('h2'):
#     print('\n Tilulo: ', titulo.text.strip())
#     for link in titulo.find_next_siblings('p'):
#         for a in link.find_all('a', href=True):
#             print('\n Texto link: ', a.text.strip(), '| URL:', a["href"])

# def enviar_arquivo():
#     # Caminho do arquivo para uploud
#     caminho = r'C:/Users/thiag/Downloads/produtos_informatica.xlsx'
#
#     # Enviar o arquivo
#     requisicao = requests.post(url = 'https://file.io', files = {'file': open(caminho, 'rb')})
#     saida_resquisicao = requisicao.json()
#
#     print(saida_resquisicao)
#     url = saida_resquisicao['link']
#     print("Arquivo. Link para acesso: ", url)
#
# def enviar_arquivo_chave():
#
#     # caminho do arquivo e chave para uploud
#     caminho = r'C:/Users/thiag/Downloads/produtos_informatica.xlsx'
#     chave_acesso = 'ASFG2JN.8E21MKE-WFQ4RZ4-M6SFV4F-80GSNHJ' # API KEY
#
#     # Enviar o arquivo
#     requisicao = requests.post(
#         url = 'https://file.io',
#         files={'file': open(caminho, 'rb')},
#         headers={'Authorization': chave_acesso}
#     )
#     saida_requisicao = requisicao.json()
#
#     print(saida_requisicao)
#     url = saida_requisicao['link']
#     print("Arquivo enviado com chave. link para acesso:", url)

# def receber_arquivo(file_url):
#     #receber o arquivo
#     requisicao = requests.get(file_url)
#
#     #Salvar o arquivo
#     if requisicao.ok:
#         with open('arquivo_baixado.xlsx', 'wb') as file:
#             file.write(requisicao.content)
#         print("Arquivo baixado com sucesso. ")
#     else:
#         print("Erro ao baixar o arquivo", requisicao.json())
#
#
# enviar_arquivo()
# enviar_arquivo_chave()
# # receber_arquivo('https://www.file.io/imUm/download/Uw0H03oZHUn4')