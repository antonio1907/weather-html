import requests
import json
from jinja2 import Template
import webbrowser

def orientaciondelviento(direccion):
	if direccion >= 337.5 and direccion < 22.5:
		return "Norte"
	if direccion >= 22.5 and direccion < 67.5:
		return "Noreste"
	if direccion >= 67.5 and direccion < 112.5:
		return "Este"
	if direccion >= 112.5 and direccion < 157.5:
		return "Sureste"
	if direccion >= 157.5 and direccion < 202.5:
		return "Sur"
	if direccion >= 202.5 and direccion < 247.5:
		return "Suroeste"
	if direccion >= 247.5 and direccion < 292.5:
		return "Oeste"
	if direccion >= 292.5 and direccion < 337.5:
		return "Noroeste"

ciudades=["Almeria", "Cadiz", "Cordoba", "Granada", "Huelva", "Jaen", "Malaga", "Sevilla"]
temperatura_min = []
temperatura_max = []
velocidad_viento = []
direccion_viento = []
print ''

f = open('plantilla.html','r')

html = ' '

for linea in f:
	html += linea

plantilla = Template(html)


for ciudad in ciudades:
	respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudad})
	dicc = json.loads(respuesta.text)


	tempemin = round(dicc["main"]["temp_min"] - 273,1)
	temperatura_min.append(tempemin)
	tempemax = round(dicc["main"]["temp_max"] - 273,1)
	temperatura_max.append(tempemax)
	viento = round(dicc["wind"]["speed"] * 1.61,1)
	velocidad_viento.append(viento)
	direccion = dicc["wind"]["deg"]
	direccion_viento.append(orientaciondelviento(direccion))

tiempo = plantilla.render(ciudad=ciudades,temp_max=temperatura_max,temp_min=temperatura_min,speed=velocidad_viento,direccion=direccion_viento)
fichero = open('tiempo.html','w')
fichero.write(tiempo)
fichero.close()
webbrowser.open("tiempo.html")
