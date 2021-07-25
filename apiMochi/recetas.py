import requests
from bs4 import BeautifulSoup

def getRecetas(ingredientes, n = 5):
    
    url ='https://www.recetasgratis.net/busqueda?q='+ingredientes
    request = requests.get(url)
    soup = BeautifulSoup(request.text,'html.parser')
    Recetas = soup.select(".resultado")
    ListRecetas=[]
    for rec in Recetas[0:n]:
        aux={}
        RecetaInfo = rec.find('img')["alt"]

        ImagReceta= rec.find('img')["src"]

        RecetaEnlace =rec.find('a')["href"]

        RecetaIntro = soup.select(".intro")
        RecetaIntro=rec.text.replace("\n","")

        aux = dict(nombre=RecetaInfo,imagen=ImagReceta,Enlace=RecetaEnlace,Intro=RecetaIntro)
        ListRecetas.append(aux)
        
    return ListRecetas


    