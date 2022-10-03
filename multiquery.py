import pyodbc 
import mysql.connector
import pandas as pd

#
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
                      'PWD=Samir102022')

c_sqlsrv = db_source.cursor()
c_mysql = db_destiny.cursor()
c_mysql.execute("SELECT clientName FROM cvbill_prd.clientes where clientName like 'CLPADSASR001%' order by clientName ")
r_mysql = c_mysql.fetchall()

# Query parameters
query = "SELECT id,name,displayName,net_hostname,csHostName,GUID FROM commserv.[dbo].[APP_Client] WHERE name like '{}%'"

pesquisa = None

for x in r_mysql:
    pesquisa = x[0]
    print("Select:")
    print(query.format(pesquisa))
    c_sqlsrv.execute(query.format(pesquisa))
    r_sqlsrv = c_sqlsrv.fetchall()
    for z in r_sqlsrv: 
        print(z)
    