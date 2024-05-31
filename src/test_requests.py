import requests
from utilitaires import file

url = "https://codeavecjonathan.com/scraping/techsport/index.html?id=dynamic-pulse"
#Je ne peux pas scraper car il y' a du code javascript.
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}




response = requests.get(url, headers = HEADERS)
response.encoding = response.apparent_encoding



if response.status_code == 200: 
    html = response.text
    #print(html) VÉRIFICATION DU FICHIER HTML
    file("res/techsport.html",html,"w")

else: 
    print("Erreur : ", response.status_code)

print("Fin de la manoeuvre")