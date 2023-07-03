#Importo la libreria JSON
import json
from urllib.request import urlopen #Mi serve per poter collegre un sito esterno

json_ex = '{"nome" : "Michele", "eta":43,"citta":"Caserta"}'

#parse json
json_parse = json.loads(json_ex)

print(json_parse["nome"])

#Esempio con JSON esterno
#vado a prendere il sito che contiene la risorsa json
url = "http://www.formatlearning.com/wp-json/wp/v2/posts"

#vado a conservare i dati in una variabile
response = urlopen(url)

#converto i dati caricati in json
json_data = json.loads(response.read())

print(type(json_data))
print(len(json_data))
print(type(json_data[0]))
print(json_data[0].get("slug"))

#Scorro la lista e stampo tutti gli slug
for el in json_data:
    #print(el["title"]["rendered"])
    print(el.get("title").get("rendered"))

#Creare un file JSON
alunno1 = {
    "nome" : "Silvia",
    "cognome" : "Drea"
}

alunno2 = {
    "nome" : "Enza",
    "cognome" : "Macrì"
}

classe = [alunno1, alunno2]
print(classe)

file_json = open("file_esempio.json", "w")
file_dump = json.dumps(classe)#Formatto i dati in JSON
print(file_dump)
file_json.write(file_dump)
file_json.close()