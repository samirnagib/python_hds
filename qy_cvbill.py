from uuid import UUID
import pyodbc 
import mysql.connector
import pandas as pd
import time

# autenticação no banco
db_destiny = mysql.connector.connect(
  host="192.168.175.109",
  user="script",
  password="Globo102022",
  database="cvbill_prd",
  auth_plugin='mysql_native_password'
)

db_source = pyodbc.connect('Driver={SQL Server};'
                      'Server=CMAY22WB01.globoi.com\HDPS;'
                      'Database=commserv;'
                      'Trusted_Connection=no;'
                      'UID=script;'
                      'PWD=Samir102022;'
                      'unicode_results=True')
db_source.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8' )
db_source.setencoding(encoding='utf-8')

#cria os cursores dos bancos
c_sqlsrv = db_source.cursor()
c_mysql = db_destiny.cursor()

#querys de consulta
# simula a leitura dos dados do relatório recebidos via api
qy_destiny_sel_rp = "SELECT distinct Client FROM cvbill_prd.rel_charge where Client like 'rj2%' order by Client"# limit 10;"
#busca os dados na base cvbill os clientes 
qy_destiny_sel_cn = "SELECT idClient, clientName, UUID FROM cvbill_prd.clientes where clientName like '{}%' order by clientName"
qy_destiny_sel_id = "SELECT idClient, clientName, UUID FROM cvbill_prd.clientes where UUID='{}' order by clientName"
qy_destiny_upd = "UPDATE clientes SET UUID='{}' WHERE ( idClient = '{}');"
qy_source = "SELECT id,displayName,GUID FROM commserv.[dbo].[APP_Client] WHERE displayName like '{}%'"

#print(qy_destiny_sel_cn.format(server_valor))
#c_mysql.execute(qy_destiny_sel_cn.format(server_valor))
# Executa as leituras dos dados do relatorio
c_mysql.execute(qy_destiny_sel_rp)
r_mysql = c_mysql.fetchall()



#para cada item na pesquisa do relatório
for x in r_mysql:
    #print("Executanto a pesquisa do serviror: ", x[0])
    #print(qy_source.format(x[0]))
    #pesquisa o nome do servidor na base do commvault para receber o UUID
    c_sqlsrv.execute(qy_source.format(x[0]))
    r_sqlsrv = c_sqlsrv.fetchone()
    # guarda as informações do servidor e do uuid
    server_valor = r_sqlsrv[1]
    server_uuid = r_sqlsrv[2]
    #print(server_valor)
    #print(server_uuid)
    
    #pesquisa na base do cvbill o server pelo uudi
    print(qy_destiny_sel_id.format(server_uuid))
    c_mysql.execute(qy_destiny_sel_id.format(server_uuid))
    r_mysql2 = c_mysql.fetchone()
    if r_mysql2 != None:
      #encontra procede com a inserção dos dados
      for server in r_mysql2:
        print("Servidor Encontrado")
        print(r_mysql2)
        time.sleep(0.5)
    else:
      # cadastra o novo servidor
      print("Cadastrando Novo Servidor")
      time.sleep(2.5)

