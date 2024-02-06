import pandas
#from icecream import ic 
import requests
from datetime import datetime
import json

url = "http://localhost:8080/Patient"
headers = {"Accept": "application/fhir+json"}


dados_csv = pandas.read_csv('dados/patients.csv')

#ic(dados_csv)


for index, row in dados_csv.iterrows():
    if row['Gênero'] == 'Masculino':
        genero = 'male'
    elif row['Gênero'] == 'Feminino':
        genero = 'female'
    else:
        genero = 'unknow'
    birth_date = datetime.strptime(row['Data de Nascimento'], '%d/%m/%Y').strftime('%Y-%m-%d')
    data = {
  "resourceType" : "Patient",
  "identifier" : [{ 'type': 'TAX', 'value': row['CPF'] }],
  "active" :True,
  "name" : [{ 'text': row['Nome'] }],
  "telecom" : [{ 'phone': row['Telefone'] }],
  "gender" : genero, 
  "birthDate" : birth_date,
  "birthCountry": [{ 'code' : '10' }],
    }
    json_data = json.dumps(data)

    response = requests.post(url, headers=headers, json=json_data)
   #ic(data)




