import requests
from bs4 import BeautifulSoup
import time 
request=requests.get('https://www.worldometers.info/geography/alphabetical-list-of-countries/')
fecha = time.strftime("%Y-%m-%d")
url = "https://covid-19-data.p.rapidapi.com/report/country/name"
soup = BeautifulSoup(request.text,'html.parser')
paises = soup.select('tr')[1:]
paises_=[]
for pais in paises:
    paises_.append(pais.findAll('td')[1].text)
    
def infoCovid(paises_):
    pais_covid=[]
    for p in paises_:
        querystring = {"name":p,"date":"2020-04-01"}
        headers = {
            'x-rapidapi-key': "cd43a834admshd3111bb758ceba7p121ec8jsnf8f6d49ab74f",
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        pais_covid.append(response.json()[0])
        time.sleep(1)#hay que esperar para hacer mas consultas de varios paises
    return pais_covid

def tabla(pais_covid):
    for total in pais_covid:
        provinces = total['provinces'][0]
        del(total["provinces"])
        total.update(provinces)
    return pais_covid

pais_covid=infoCovid(paises_[0:9])
pais_covid=tabla(pais_covid)

pd.DataFrame(pais_covid)
