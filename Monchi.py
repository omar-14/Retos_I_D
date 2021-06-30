Recetas = soup.select(".resultado")
ListRecetas=[]
for rec in Recetas:
    aux={}
    RecetaInfo = rec.find('img')["alt"]
    
    ImagReceta= rec.find('img')["data-imagen"]
    
    RecetaEnlace =rec.find('a')["href"]
    
    RecetaIntro = soup.select(".intro")
    RecetaIntro=rec.text.replace("\n","")
   
    aux = dict(nombre=RecetaInfo,imagen=ImagReceta,Enlace=RecetaEnlace,Intro=RecetaIntro)
    ListRecetas.append(aux)

for i in range(len(ListRecetas)):
    print(i+1,"- "+ListRecetas[i]["nombre"])
    
elije_receta=int(input("Elige una receta: "))
elije_receta=elije_receta-1
url=ListRecetas[elije_receta]["Enlace"]
nueva = requests.get(url)
Nsoup = BeautifulSoup(nueva.text,'html.parser')
Titulo=Nsoup.title.text
clear_output(wait=True)


Receta=[]
print(url)
#introduccion de receta
Introduccion = Nsoup.select('.intro')
ImagenIntro= Introduccion[0].find('img')['src']
Intro=Introduccion[0].text.replace("\n","")
IntroReceta=dict(nombreR=ListRecetas[elije_receta]["nombre"],imagen=ImagenIntro,Introtext=Intro)
Receta.append(IntroReceta)

#infromacio de receta
InfoIngr = Nsoup.select('.property')
personas = InfoIngr[0].text
tiempo = InfoIngr[1].text
tipoPlato = InfoIngr[2].text
dificultad = InfoIngr[3].text
adicionales = Nsoup.select('.inline')[0].text.replace("\n"," ")
info = dict(personas=personas, tiempo=tiempo, plato=tipoPlato, dificultad=dificultad,caracteristicas=adicionales)
Receta.append(info)

#lista de ingredientes
ListIngredientes=[]
Ingredientes = Nsoup.select(".ingrediente")
for ingrediente in Ingredientes:
    ingr = ingrediente.find('label')
    if(ingr == None):
        continue
    ingr=ingr.text.replace("\n","")
    ListIngredientes.append(ingr)
aux=dict(ingredientes=ListIngredientes)
Receta.append(aux)
    
#pasos para realizar la receta
Pasos_=[]
pasos = Nsoup.select('.apartado')

for paso in pasos[:-2]:
    instruc = paso.text.replace("\n"," ")
    Pasos_.append(instruc)

Preparacion=[]
i=0
for img in pasos:
    imagen = img.find('img')
    #print(type(imagen))
    if(imagen == None):
        continue
    instruccion=dict(paso=Pasos_[i],imagen=imagen["src"])
    i=i+1
    Preparacion.append(instruccion)
prepara=dict(Intrucciones=Preparacion)
Receta.append(prepara)


for i in range(len(Receta)):
        for clave in Receta[i]:
            #print(type(Receta[i]))
            if type(Receta[i])==dict:
                if(clave=="caracteristicas"):
                    print("Información de la receta: \n")
                    print(Receta[i][clave]+"\n")
                elif(clave=="ingredientes"):
                    print("Ingredientes: \n")
                    for j in range(len(Receta[i][clave])):
                        print(Receta[i][clave][j])
                    print("\n")
                elif(clave=="Intrucciones"):
                    print("Intrucciones: \n")
                    for o in Receta[i][clave]:
                        for n in o:
                            print(o[n]+"")
                        print("\n")
                else:
                    print(Receta[i][clave]+"\n")
                
                
            
                


   