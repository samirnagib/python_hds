from itertools import count
import requests
import sys
import xml.etree.ElementTree as ET
import base64
import json
import pandas as pd
import datetime
import pyodbc 
import mysql.connector

# conexões com os banco de dados
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




# autenticação no commvault
senha = None
url = "http://cmay22wb01.globoi.com:81/SearchSvc/CVWebService.svc/Login"
headers = {"Content-Type": "application/json; charset=utf-8"}
data = {
    "username":"Samir",
    "password":"IVJ2MzB0QXoj",
}
R = requests.post(url,headers=headers ,json=data)
print("Status Code:", R.status_code)

token = None

if R.status_code == 200:
    root = ET.fromstring(R.text)
    if 'token' in root.attrib:
        token = root.attrib['token']
        print("Login feito com sucesso")
        # recupera o token de acesso
        senha = token[5:]
    else:
        print("Falha na autenticação")
else:
   print ('there was an error logging in')


#Buscas as informações de chargeback do commvault via api

url_report = "http://cmay22wb01.globoi.com/webconsole/api/cr/reportsplusengine/datasets/METRICS_DEFAULT/data?livefeed=true&parameter.param8=4&parameter.param9=0&offset=0&dateFormat=milliseconds&priority=normal&nullValue=&syscol=false&parameter.param10=&limit=-1&parameter.param2=5&parameter.param3=0&parameter.param1=-1&parameter.param11=&parameter.param6=TB&operation=METRICS_EXECUTE_SP&parameter.param7=NULL&parameter.spName=RptMonthlyStorageUsage&parameter.param4=1&parameter.param5=2022-10-01 00:00:00"
report_headers = { "Accept":"application/json", "AuthToken":senha}
AIO = requests.get(url_report,headers=report_headers)
print("Status Code:", AIO.status_code)
report_data = json.loads(AIO.content)

# variaaveis para receber os dados da api
Billing_Tag = []
Tag_Notes = []
CommServ_UniqueId = []
CommCell_Name = []
Client_Groups = []
Client = []
Agent = []
Instance = []
Backupset = []
Subclient = []
Storage_Policy = []
Copy = []
Front_End_Backup_Size = []
Front_End_Backup_Cost = []
Front_End_Archive_Size = []
Front_End_Archive_Cost = []
Primary_App_Size = []
Primary_App_Cost = []
Protected_App_Size = []
Protected_App_Cost = []
Media_Size = []
Media_Cost = []
Total_Cost = []
Copy_Type = []
Client_UUID = [] 
cont =0
#populando do dados vindo da api
for y in report_data['records']:
    Billing_Tag.append(y[0])
    Tag_Notes.append(y[1])
    CommServ_UniqueId.append(y[2])
    CommCell_Name.append(y[3])
    Client_Groups.append(y[4])
    Client.append(y[5])
    Agent.append(y[6])
    Instance.append(y[7])
    Backupset.append(y[8])
    Subclient.append(y[9])
    Storage_Policy.append(y[10])
    Copy.append(y[11])
    Front_End_Backup_Size.append(y[12])
    Front_End_Backup_Cost.append(y[13])
    Front_End_Archive_Size.append(y[14])
    Front_End_Archive_Cost.append(y[15])
    Primary_App_Size.append(y[16])
    Primary_App_Cost.append(y[17])
    Protected_App_Size.append(y[18])
    Protected_App_Cost.append(y[19])
    Media_Size.append(y[20])
    Media_Cost.append(y[21])
    Total_Cost.append(y[22])
    Copy_Type.append(y[23]) 
    
    #pesquisa na base de dados da commvault
    c_sqlsrv = db_source.cursor()
    # Query parameters
    qy_source = "SELECT name,GUID FROM commserv.[dbo].[APP_Client] WHERE name like '{}%'"
    pesquisa = None
    pesquisa = y[5]
    #print(query.format(pesquisa))
    c_sqlsrv.execute(qy_source.format(pesquisa))
    r_sqlsrv = c_sqlsrv.fetchall()
    
    for z in r_sqlsrv: 
        print("Contador: ", str(cont) )
        Client_UUID.append(z[1])
        print("CLIENTE.: ",y[5]," UUID.: ", z[1])
        cont = cont+1
        qy_destiny_sel = None
        qy_destiny_upd = None


















# parte para gerar uma listagem 
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_cols', None)
rel_charge = pd.DataFrame(
    list(zip(Billing_Tag,Client,Instance,Backupset,Subclient,Storage_Policy,Copy,Front_End_Backup_Size,Front_End_Archive_Size,Primary_App_Size,Protected_App_Size,Media_Size)),
    columns=['Billing Tag','Client','Instance','Backupset','Subclient','Storage_Policy','Copy','FEB Size','FEA Size','Primary AppSize','Protected App Size', 'Media Size']
)

#VERSÃO REDUZIDA
#rel_charge = pd.DataFrame(
#    list(zip(Client)),
#    columns=['Client']
#)

dataf = datetime.datetime.now()
arq = "rel_charge_"+dataf.strftime("%Y%m%d_%H%M%S")+".csv"

#print(rel_charge)
rel_charge.to_csv(arq,index=False)
#with open('relat.txt', 'w') as f:
#    f.write(str(rel_charge))
#f.close()
