#Solicitud de un endpoint sin argumentos
#primero importamos la biblioteca
import requests # type: ignore
import json
URL = "https://weatherstack.com/users"

respuesta = requests.get(URL)

if respuesta.status_code == 200:
   print('Solicitud exitosa')
   print('Datos:', respuesta.json())
else:
    print("Error en la solicitud del recurso. Detalles",
          respuesta.text) 
#imprimir respuesta
respuesta_json = respuesta.json ()