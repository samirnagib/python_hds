from uuid import UUID
import pyodbc 
import mysql.connector
import pandas as pd

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
                      'PWD=Samir102022')

c_sqlsrv = db_source.cursor()

server_valor = "CLPADSASR001"
server_uuid = "5979912B-586D-4365-9DA4-4C3DC4F0FF3D"

c_mysql = db_destiny.cursor()


qy_destiny_sel_cn = "SELECT idClient, clientName, UUID FROM cvbill_prd.clientes where clientName like '{}%' order by clientName"
qy_destiny_sel_id = "SELECT idClient, clientName, UUID FROM cvbill_prd.clientes where UUID='{}' order by clientName"
qy_destiny_upd = "UPDATE clientes SET UUID='{}' WHERE ( idClient = '{}');"

#print(qy_destiny_sel_cn.format(server_valor))
c_mysql.execute(qy_destiny_sel_cn.format(server_valor))
r_mysql = c_mysql.fetchall()

#print("Tamanho resultado da query: ", len(r_mysql))

for x in r_mysql:
    server_i = x[0]
    server_n = x[1]
    server_u = x[2]
    
    print(server_i)
    print(server_n)
    print(server_u)
    
    if server_n != None :
        print("Server name found")
        if server_u != None :
            print("Server UUID found")
        else:
            print("Server UUID NOT found".upper())
            print(qy_destiny_upd.format(server_u,server_i))
            #c_mysql.execute(qy_destiny_upd.format(server_u,server_i))
    else:
        print("Server name not found".upper())
    #print("tamanho do Campo UUID", len(x[1]))
  

#print(qy_destiny_sel_id.format(server_uuid))  
#c_mysql.execute(qy_destiny_sel_id.format(server_uuid))
#r_mysql = c_mysql.fetchall()

#print("Tamanho resultado da query: ", len(r_mysql))
#for z in r_mysql:
#    print(z)
