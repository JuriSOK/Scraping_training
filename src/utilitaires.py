
from bs4 import BeautifulSoup

#Pour créer le fichier html
def file(destination,contenu,droit):
    f = open(destination,droit)
    f.write(contenu)
    f.close

#on vérifie si e existe, si oui on affiche son texte, sinon on retourne None
def get_text_if_not_none(e):
    if e:
        return e.text.strip()
    return None