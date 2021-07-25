from flask import Flask
from flask import jsonify
import recetas

app = Flask(__name__)
keys = {"123d454"}

@app.route('/api/monchi/key=<key>&ingredientes=<ingredientes>&numero=<numero>', methods = ["GET"])
def f(key,ingredientes,numero):
    if key not in keys:
        return jsonify({"eror":"errorkey"})
    
    ingredientes=ingredientes.replace(" ","+")
    
    datos = recetas.getRecetas(ingredientes,int(numero))
    
    response = {
                'status':'success',
                'datos':datos
               }
    return jsonify(response)


@app.route('/api/monchi/key=<key>&ingredientes=<ingredientes>', methods = ["GET"])
def g(key,ingredientes):
    if key not in keys:
        return jsonify({"eror":"errorkey"})
    
    ingredientes=ingredientes.replace(" ","+")
    
    datos = recetas.getRecetas(ingredientes)
   
    response = {'status':'success',
                'datos':datos
               }
    return jsonify(response)

@app.route('/api/id=<id>', methods = ["GET"])
def h(id):
    response = {'menssage':'success','id':id}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug = True)
