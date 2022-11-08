import requests
import sys
import xml.etree.ElementTree as ET
import base64
import json
import pandas as pd

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
        #print(token)
        # print(token[5:]) # token sem o QSDK
        senha = token[5:]
        
        print(senha)


    else:
        print("Falha na autenticação")
else:

   print ('there was an error logging in')



#Parte do relatorio

