import json

with open("bibliotheque.json") as f:
    file=json.load(f)

livres= file["livres"]
magazines=file["magazines"]
dvds=file["dvds"]

#Fonction pour ajouter une entité dans la bibliothéque
auteurs=[]
def ajout_bib():
    """
    Cette fonction permet d'ajouter une nouvelle entité dans la bibliothèque
    """

    #On remplit les informations d'une entité
    titre=input("Donner le titre : ")
    auteurs=input("Donner les auteurs : ")
    while True:
        annee=input("Donner l'année de sortie: ")
        if annee.isdigit() and len(annee)==4:
            break
    while True:
        isbn=input("Donner l'ISBN de livre: ")
        if isbn.isdigit() and len(isbn)==13:
            break
    description=input("Donner la description : ")
    categorie=input("Donner la categorie : ")
    while True:
        nbexp=input("Donner le nombre des exemplaires : ")
        if nbexp.isdigit() and int(nbexp)>=0:
            break
    while True:
        page=input("Donner le nombre des pages: ")
        if page.isdigit() and int(page)>0:
            break
    editeur=input("Donner l'éditur: ")

    #On doit choisir le type d'entité pour savoir où on va placer la nouvelle entité
    while True:
        entite=input("Donner le type d'entité à ajouter (choissez (livre/magazine/dvd)):\n")
        if entite=="livre" or entite=="magazine" or entite=="dvd":
            break
    match entite:
        case "livre":
            nv_entite= {
                "titre": titre,
                "auteurs": auteurs,
                "annee": annee,
                "ISBN": isbn,
                "description": description,
                "categorie": categorie,
                "nombre_exemplaires": nbexp,
                "pages":page,
                "editeur": editeur
            }
            livres.append(nv_entite)
        case "magazine":
            nv_entite = {
                "titre": titre,
                "auteurs": auteurs,
                "annee": annee,
                "description": description,
                "categorie": categorie,
                "nombre_exemplaires": nbexp,
                "pages": page,
                "editeur": editeur
            }
            magazines.append(nv_entite)
        case "dvd":
            nv_entite = {
                "titre": titre,
                "auteurs": auteurs,
                "annee": annee,
                "description": description,
                "categorie": categorie,
                "nombre_exemplaires": nbexp,
                "editeur": editeur
            }
            dvds.append(nv_entite)
    with open("bibliotheque.json","w") as f:
        json.dump(file, f)

#Fonction pour supprimer une entité
def supprime_bib():
    """
    Cette fonction permet de supprimer une entité de la bibliothèque
    """
    while True:
        entite=input("Donner le type d'entité à supprimer (choissez (livre/magazine/dvd)):\n ")
        if entite=="livre" or entite=="magazine" or entite=="dvd":
            break
    titre=input("Donner le titre à supprimer: ")
    match entite:
        case "livre":
            for livre in livres:
                if livre["titre"]==titre:
                    livres.remove(livre)
                    with open("bibliotheque.json","w") as f:
                        json.dump(file, f)
                    break
        case "magazine":
            for magazine in magazines:
                if magazine["titre"] == titre:
                    magazines.remove(magazine)
                    with open("bibliotheque.json", "w") as f:
                        json.dump(file, f)
                    break
        case "dvd":
            for dvd in dvds:
                if dvd["titre"] == titre:
                    dvds.remove(dvd)
                    with open("bibliotheque.json", "w") as f:
                        json.dump(file, f)
                    break

#Fonction pour modifier les informations d'une entité
def modifier_bib():
    """
    Cette fonction permet de modifier les informations d'une entité de la bibliothèque
    """
    while True:
        entite=input("Donner le type d'entité que vous voulez le modifier (choissez (livre/magazine/dvd)):\n ")
        if entite=="livre" or entite=="magazine" or entite=="dvd":
            break
    titre=input("Donner le titre pour modifier: ")
    match entite:
        case "livre":
            for livre in livres:
                if livre["titre"]==titre:
                    description = input("Donner la description de livre: ")
                    categorie = input("Donner la catégorie de livre: ")
                    while True:
                        nbexp = input("Donner le nombre des exemplaires de livre: ")
                        if nbexp.isdigit():
                            break
                    nv_entite = {
                        "titre": livre["titre"],
                        "auteurs": livre["auteurs"],
                        "annee": livre["annee"],
                        "ISBN": livre["ISBN"],
                        "description": description,
                        "categorie": categorie,
                        "nombre_exemplaires": nbexp,
                        "pages": livre["pages"],
                        "editeur": livre["editeur"]
                    }
                    livres.remove(livre)
                    livres.append(nv_entite)
                    with open("bibliotheque.json", "w") as f:
                        json.dump(file, f)
                    break
        case "magazine":
            for magazine in magazines:
                if magazine["titre"]==titre:
                    description = input("Donner la description de magazine: ")
                    categorie = input("Donner la catégorie de magazine: ")
                    while True:
                        nbexp = input("Donner le nombre des exemplaires de magazine: ")
                        if nbexp.isdigit():
                            break
                    nv_entite = {
                        "titre": magazine["titre"],
                        "auteurs": magazine["auteurs"],
                        "annee": magazine["annee"],
                        "description": description,
                        "categorie": categorie,
                        "nombre_exemplaires": nbexp,
                        "pages": magazine["pages"],
                        "editeur": magazine["editeur"]
                    }
                    magazines.remove(magazine)
                    magazines.append(nv_entite)
                    with open("bibliotheque.json", "w") as f:
                        json.dump(file, f)
                    break
        case "dvd":
            for dvd in dvds:
                if dvd["titre"]==titre:
                    description = input("Donner la description de DVD: ")
                    categorie = input("Donner la catégorie de DVD: ")
                    while True:
                        nbexp = input("Donner le nombre des exemplaires de DVD: ")
                        if nbexp.isdigit():
                            break
                    nv_entite = {
                        "titre": dvd["titre"],
                        "auteurs": dvd["auteurs"],
                        "annee": dvd["annee"],
                        "description": description,
                        "categorie": categorie,
                        "nombre_exemplaires": nbexp,
                        "editeur": dvd["editeur"]
                    }
                    dvds.remove(dvd)
                    dvds.append(nv_entite)
                    with open("bibliotheque.json", "w") as f:
                        json.dump(file, f)
                    break

#Fonction pour afficher les informations d'une entité
def affiche_bib():
    """
    Cette fonction permet d'afficher les informations d'une entité de la bibliothèque
    """
    while True:
        entite=input("Donner le type d'entité que vous voulez l'afficher (choissez (livre/magazine/dvd)):\n ")
        if entite=="livre" or entite=="magazine" or entite=="dvd":
            break
    titre=input("Donner le titre pour l'afficher: ")
    match entite:
        case "livre":
            for livre in livres:
                if livre["titre"] == titre:
                    res = "\ntitre: {} \nauteurs: {} \nannée: {}\nISBN: {} \ndescription: {} \ncategorie: {} \nnombre_exemplaires: {} \npages: {} \néditeur: {} \n"
                    print(res.format(livre["titre"],livre["auteurs"],livre["annee"],livre["ISBN"],livre["description"],livre["categorie"],livre["nombre_exemplaires"],livre["pages"],livre["editeur"]))
        case "magazine":
            for magazine in magazines:
                if magazine["titre"] == titre:
                    res = "\ntitre: {} \nauteurs: {} \nannée: {} \ndescription: {} \ncategorie: {} \nnombre_exemplaires: {} \npages: {} \néditeur: {} \n"
                    print(res.format(magazine["titre"], magazine["auteurs"], magazine["annee"], magazine["description"], magazine["categorie"], magazine["nombre_exemplaires"], magazine["pages"], magazine["editeur"]))
        case "dvd":
            for dvd in dvds:
                if dvd["titre"] == titre:
                    res = "\ntitre: {} \nauteurs: {} \nannée: {} \ndescription: {} \ncategorie: {} \nnombre_exemplaires: {} \néditeur: {} \n"
                    print(res.format(dvd["titre"], dvd["auteurs"], dvd["annee"], dvd["description"], dvd["categorie"], dvd["nombre_exemplaires"], dvd["editeur"]))

#Fonction pour afficher toute la bibliotheque
def affichage_tous_bib():
    """
    Cette fonction permet d'afficher toutes les entités de la bibliothèque
    """
    for livre in livres:
        res = "\ntitre: {} \nauteurs: {} \nannée: {}\nISBN: {} \ndescription: {} \ncategorie: {} \nnombre_exemplaires: {} \npages: {} \néditeur: {} \n"
        print(res.format(livre["titre"], livre["auteurs"], livre["annee"], livre["ISBN"], livre["description"], livre["categorie"], livre["nombre_exemplaires"], livre["pages"], livre["editeur"]))
    for magazine in magazines:
        res = "\ntitre: {} \nauteurs: {} \nannée: {} \ndescription: {} \ncategorie: {} \nnombre_exemplaires: {} \npages: {} \néditeur: {} \n"
        print(res.format(magazine["titre"], magazine["auteurs"], magazine["annee"], magazine["description"], magazine["categorie"], magazine["nombre_exemplaires"], magazine["pages"], magazine["editeur"]))
    for dvd in dvds:
        res = "\ntitre: {} \nauteurs: {} \nannée: {} \ndescription: {} \ncategorie: {} \nnombre_exemplaires: {} \néditeur: {} \n"
        print(res.format(dvd["titre"], dvd["auteurs"], dvd["annee"], dvd["description"], dvd["categorie"], dvd["nombre_exemplaires"], dvd["editeur"]))
