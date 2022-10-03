import pyodbc 
import pandas as pd

#conn = pyodbc.connect('Driver={SQL Server};'
#                      'Server=192.168.172.109;'
#                      'Database=commserv;'
#                      'Trusted_Connection=no;'
#                      'UID=script;'
#                      'PWD=Samir102022')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=CMAY22WB01.globoi.com\HDPS;'
                      'Database=commserv;'
                      'Trusted_Connection=no;'
                      'UID=script;'
                      'PWD=Samir102022')




#cursor = conn.cursor()
#cursor.execute('SELECT id,name,displayName,net_hostname,csHostName,GUID FROM commserv.[dbo].[APP_Client] ORDER BY name')

df = pd.read_sql_query('SELECT id,name,displayName,net_hostname,csHostName,GUID FROM commserv.[dbo].[APP_Client] ORDER BY name',conn)


#for i in cursor:
#    print(i)

print(df)