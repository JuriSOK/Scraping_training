import requests
from bs4 import BeautifulSoup
from utilitaires import file
from utilitaires import get_text_if_not_none
from urllib.parse import urljoin

def main():
    print("Vous êtes dans le main")

    url = "https://codeavecjonathan.com/scraping/recette/"
    response = requests.get(url)
    response.encoding = response.apparent_encoding


    if response.status_code == 200: 
        html = response.text
        #print(html) VÉRIFICATION DU FICHIER HTML
        file("recette.html",html,"w")

        soup = BeautifulSoup(html, "html5lib") #ON APPELLE LE CONSTRUCTEUR BEAUTIFUL SOUP AVEC LE PARSEUR

        #TITRE_____
        titre = get_text_if_not_none(soup.find("h1")) #ON CHERCHE LE TITRE QUI EST DANS UNE BALISE H1
        print(titre)

        #DESCRIPTION_____
        description = get_text_if_not_none(soup.find("p", class_ = "description")) #ON CHERCHE LA DESCRIPTION QUI EST DANS UNE BALISE P + CLASSE DESCRIPTION
        print(description)

        #INGRÉDIENT_____
        #On isole avant tout ce qu'il y'a dans le div de classe Ingredients
        div_ingredients = soup.find("div",class_ = "ingredients")
        #On prend tout les ingredients
        ingredients = div_ingredients.find_all("p")

        #On affiche les ingrédients.
        for ingredient in ingredients:
            print("Ingrédient : ",get_text_if_not_none(ingredient))

        #ÉTAPE DE PRÉPARATION_____
        table_etapes = soup.find("table",class_ = "preparation")
        etapes = table_etapes.find_all("td",class_ = "preparation_etape")
        etapes_number = table_etapes.find_all("p",class_ = "numero")

        #Pour itérer en meme temps
        for number,etape in zip(etapes_number,etapes):
            print("Etape ", get_text_if_not_none(number), " ", get_text_if_not_none(etape))
        
        #IMAGE DE GATEAU_____
        #On doit donner le chemin absolu donc on fait url + chemin relatif de l'image
        image_url = urljoin(url,soup.find("img",class_ = "centre info")["src"]   )    
        #On obtient l'image
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
           #image_response_content permet d'avoir l'image réelle
           file("gateau.jpg",image_response.content,"wb")
        else: 
            print("Erreur : ", response.status_code)

        #Informations
        table_info = soup.find("table",class_ = "info")
        infos_header = table_info.find_all("th")
        infos_valeur = table_info.find_all("td")

        #On a besoin d'itérer en même temps, pour cela on utilise zip() en Python

        for info,valeur in zip(infos_header,infos_valeur):
            print(get_text_if_not_none(info), " : " ,get_text_if_not_none(valeur))


    else: 
        print("Erreur : ", response.status_code)

    print("Fin de la manoeuvre")


if __name__ == "__main__":
    main()









