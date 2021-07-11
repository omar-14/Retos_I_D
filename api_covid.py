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
        if response.status_code==200:
            total=response.json()[0]
            provinces = total['provinces'][0]
            del(total["provinces"])
            total.update(provinces)
            pais_covid.append(total)            
            time.sleep(1)#hay que esperar para hacer mas consultas de varios paises
        else:
            print("Error, no recibimos respuesta")
            break
    
    return pais_covid

pais_covid=infoCovid(paises_[0:3])
pd.DataFrame(pais_covid)
