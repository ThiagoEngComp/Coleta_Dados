import pymysql
import pandas as pad

from sqlalchemy import create_engine

def conexao_mysql(host, user, password, db, table):
    #Criar conexao
    conn = pymysql.connect(host=host, user=user, password=password, db=db)

    cursor = conn.cursor()

    #Executar consulta
    query = 'SELECT * FROM ' + table + ' limit 10'
    cursor.execute(query)

    #Busca Resultados
    resultados = cursor.fetchall()
    print('MySQL:')
    for linha in resultados:
        print(linha)

    cursor.close()
    conn.close()

def def_conexao_mysql(host, user, password, db, table):
    #Criar conexao
    conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + host + '/' + db)

    # Executar consultas e salvar em um dataframe
    query = 'SELECT * FROM ' + table
    df = pad.read_sql(query, conn)

    # Exibir os resultados
    print('Tabela MySQL com DataFrame: \n', df.head())

    # Fecha conexao
    conn.dispose()
    return df

def conexao_exel(path):
    #Ler arquivo Excel
    df = pad.read_excel(path)
    print('Dados Excel: \n', df.head())

    # Escrever arquivo CSV
    df.to_csv(path_or_buf='dados.csv', index=False)

def conexao_csv(path):
    #Ler arquivo CSV
    df = pad.read_csv(path)
    print('Dados CSV: \n', df.head())

    # Escrever arquivo JSON
    df.to_json(path_or_buf='dados.json', orient='records', index=False)

conexao_mysql(host='localhost', user='root', password='1312', db='loja_informatica', table='cliente')

df_cliente = def_conexao_mysql(host='localhost', user='root', password='1312', db='loja_informatica', table='cliente')
df_cliente.to_excel(excel_writer='dados.xlsx', index=False)

conexao_exel('dados.xlsx')
conexao_csv('dados.csv')
