
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="cmay22wb27.globoi.com",
  user="script",
  password="Globo102022",
  database="cvbill_prd",
  auth_plugin='mysql_native_password'
)


mycursor = mydb.cursor()


mycursor.execute('SELECT * FROM cvbill_prd.billtags')

myresult = mycursor.fetchall()

for x in myresult:
    print(x[0])
    print(x[1])
    print(x[2])
    
#df = pd.read_sql_query('SELECT * FROM cvbill_prd.billtags',mydb)

#print(df)