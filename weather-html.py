import requests
import json

print """
'''
1.Almeria
2. Cadiz
3. Cordoba
4. Granada
5. Huelva
6. Jaen
7. Malaga
8. Sevilla

"""
ciudades={1:"Almeria", 2:"Cadiz", 3:"Cordoba", 4:"Granada", 5:"Huelva", 6:"Jaen", 7:"Malaga", 8:"Sevilla"}
ciudad=int(raw_input("De que ciudad quieres saber la temperatura actual?:"))

resultado=requests.get('http://api.openweathermap.org/data/2.5/weather', params={'q':"%s,spain"%ciudades[ciudad]})
dicc=json.loads(resultado.text)
print "la temperatura actual en", ciudades[ciudad], "es", dicc ["main"]["temp"]-273, "C"
