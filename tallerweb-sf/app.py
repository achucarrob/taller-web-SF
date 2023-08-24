# Importar Flask 
from flask import Flask, render_template
import requests
# Crear la aplicacion Flask
app = Flask(__name__)

# Crear un ruta o endpoint
@app.route("/") # ruta home
def index():
    return "Hello, My name is Achu!"

# ruta saludo
@app.route("/saludo")
def saludo():
    return render_template ("hola.html")

# crear un anueva ruta para experimentar con jinja
@app.route("/hapicat")
def hapicat():
    # definir variables
    nombre = "Hapi CAT"
    estado = "feli"
    imagen = "https://media.tenor.com/UTrLSr85tYEAAAAC/happy-cat-cat.gif"
    # pasarle a la funcion render_template() las variables como parametros, es decir entre comas
    return render_template("personaje.html", nombre = nombre , estado = estado, imagen = imagen)

# ruta personaje
@app.route("/personaje")
def consultar_personaje():
    # consultar un personaje de la API
     url = "https://rickandmortyapi.com/api/character/2"

     # Guardamos la respuesta de la API en formato json
     respuesta_api = requests.get(url).json()

     # creamos variables para acceder a las respuesta
     nombre = respuesta_api['name']
     estado = respuesta_api['status']
     imagen = respuesta_api['image']
     return render_template("personaje.html", nombre = nombre, estado = estado, imagen = imagen)