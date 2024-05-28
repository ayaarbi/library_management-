import json
import re

with open("bibliotheque.json") as f:
    file=json.load(f)

livres= file["livres"]
magazines=file["magazines"]
dvds=file["dvds"]

#Fonction de recherche par titre une expression donné par l'utilisateur
def recherche_titre(exp):
    """
    Cette fonction permet de chercher les entités dans la bibliothèque selon une expression donnée par l'utilisateur
    """
    resultat = []
    ch = re.compile(exp, re.IGNORECASE)
    for livre in livres:
        titre = livre["titre"]
        if ch.search(titre):
            resultat.append(livre)
    for magazine in magazines:
        titre = magazine["titre"]
        if ch.search(titre):
            resultat.append(magazine)
    for dvd in dvds:
        titre = dvd["titre"]
        if ch.search(titre):
            resultat.append(dvd)
    return resultat


#Fonction pour voir si un titre est disponible ou non
def disponible(exp):
    """
    Cette fonction permet de vérifier si un titre est encore disponible ou pas dans la bibliothèque
    """
    resultat = recherche_titre(exp)
    if resultat:
        for res in resultat:
            for livre in livres: #Chercher si le titre est parmi les livres de la bibliothèque
                if res["titre"] == livre["titre"]:
                    if livre["nombre_exemplaires"] == "0":
                        return ("Ce livre n'est pas disponible pour le moment, merci de choisir un nouvel titre!")
            for magazine in magazines:  #Chercher si le titre est parmi les magazines de la bibliothèque
                if res["titre"] == magazine["titre"]:
                    if magazine["nombre_exemplaires"] == "0":
                        return ("Cette magazine n'est pas disponible pour le moment, merci de choisir un nouvel titre!")
            for dvd in dvds:  #Chercher si le titre est parmi les dvds de la bibliothèque
                if res["titre"] == dvd["titre"]:
                    if dvd["nombre_exemplaires"] == "0":
                        return ("Ce DVD n'est pas disponible pour le moment, merci de choisir un nouvel titre!")

        return ("Ce titre est encore disponible, vous pouvez l'emprunter")
    else:
        return ("Titre introuvable")


