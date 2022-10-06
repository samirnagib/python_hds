import csv
import time
import mysql.connector

# autenticação no banco
db_destiny = mysql.connector.connect(
  host="192.168.175.109",
  user="script",
  password="Globo102022",
  database="cvbill_prd",
  auth_plugin='mysql_native_password'
)

c_mysql = db_destiny.cursor()
u_mysql = db_destiny.cursor()
#busca os dados na base cvbill os clientes 
qy_destiny_sel_cn = "SELECT idClient, clientName, UUID FROM cvbill_prd.clientes where clientName = '{}' order by clientName"

qy_destiny_upd = "UPDATE clientes SET UUID='{}' WHERE ( idClient = '{}');"



with open('D:\hds\python_hds\CommVault_Client_Export.csv', 'r') as file:
    arquivo = csv.reader(file, delimiter=';')
    for linha in arquivo:
        c_mysql.execute(qy_destiny_sel_cn.format(linha[1]))
        r_mysql = c_mysql.fetchone()
        if r_mysql != None:
            srv_id = r_mysql[0]
            srv_nm = r_mysql[1]
            srv_ui = r_mysql[2]
            print("Atualiando o servidor ", srv_nm, " codigo ", str(srv_id) , " com o UUID: ", linha[3])
            print(qy_destiny_upd.format(linha[3], srv_id))
            u_mysql.execute(qy_destiny_upd.format(linha[3], srv_id))
            db_destiny.commit()
            print(u_mysql.rowcount, "record(s) affected")
            #time.sleep(1)
            